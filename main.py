from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from models import StudentProfile, MentorProfile, ScoringResult, MentorMatch, SRICalculationInput, ChatMessage, Notification
from scoring import ScoringEngine
from ml import MLAssistant
import datetime

app = FastAPI(title="HEPro AI+ API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store (for demo purposes)
students_db: Dict[str, StudentProfile] = {}
mentors_db: Dict[str, MentorProfile] = {}

engine = ScoringEngine()
ml_assistant = MLAssistant()

@app.post("/students/", response_model=StudentProfile)
async def create_student(student: StudentProfile):
    students_db[student.id] = student
    return student

@app.post("/mentors/", response_model=MentorProfile)
async def create_mentor(mentor: MentorProfile):
    mentors_db[mentor.id] = mentor
    return mentor

@app.get("/scores/{student_id}", response_model=ScoringResult)
async def get_score(student_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return engine.score_student(students_db[student_id])

@app.get("/matches/{student_id}", response_model=List[MentorMatch])
async def get_matches(student_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student = students_db[student_id]
    mentors = list(mentors_db.values())
    return ml_assistant.match_mentor(student, mentors)

@app.get("/dashboard/overview")
async def get_overview():
    results = [engine.score_student(s) for s in students_db.values()]
    if not results:
        return {"total_students": 0, "average_sri": 0, "risk_counts": {}}
    
    avg_sri = sum(r.sri for r in results) / len(results)
    risk_counts = {}
    for r in results:
        risk_counts[r.risk_level] = risk_counts.get(r.risk_level, 0) + 1
        
    return {
        "total_students": len(students_db),
        "average_sri": round(avg_sri, 2),
        "risk_counts": risk_counts,
        "recent_scores": results[-5:]
    }

@app.post("/calculate-sri")
async def manual_calculate(data: SRICalculationInput):
    # Map raw input to ScoringEngine's logic
    # Mocking a profile for the calculation engine
    mock_s = StudentProfile(
        id="MOCK", name="Manual", gpa=data.gpa,
        subject_performance={"avg": data.subject_avg},
        skill_gaps=[], engagement_frequency=3, responsiveness=0.8,
        communication_preference="Auto",
        stress_level=data.stress, sleep_patterns=data.sleep,
        wellbeing_score=data.wellbeing,
        task_completion_rate=data.tasks,
        time_management_indicator=data.mgt,
        goal_clarity=data.goals,
        skill_alignment=data.alignment,
        readiness_timeline=data.timeline
    )
    result = engine.score_student(mock_s)
    return result

# In-memory chat store
chat_db: Dict[str, List[ChatMessage]] = {}

@app.get("/chat/{student_id}", response_model=List[ChatMessage])
async def get_messages(student_id: str):
    if student_id not in chat_db:
        # Initialize with a welcome message
        chat_db[student_id] = [
            ChatMessage(id="1", sender_id="M1", sender_name="Dr. Sarah Johnson", content=f"Hello {student_id}! How can I help you today?", timestamp=datetime.datetime.now().strftime("%I:%M %p"))
        ]
    return chat_db[student_id]

@app.post("/chat/{student_id}", response_model=ChatMessage)
async def post_message(student_id: str, message: ChatMessage):
    if student_id not in chat_db:
        chat_db[student_id] = []
    
    # Save student message
    chat_db[student_id].append(message)
    
    # Generate AI response (simulated)
    ai_response = ChatMessage(
        id=str(len(chat_db[student_id]) + 1),
        sender_id="AI",
        sender_name="HEPro Assistant",
        content=f"I've received your message: '{message.content}'. As your mentor, I recommend focusing on your readiness goals.",
        timestamp=datetime.datetime.now().strftime("%I:%M %p")
    )
    chat_db[student_id].append(ai_response)
    
    return message

@app.get("/notifications", response_model=List[Notification])
async def get_notifications():
    return [
        Notification(id="n1", title="Low Wellness Alert", content="Student S2 (Bob) stress level is at 80%. Consider intervention.", type="Alert"),
        Notification(id="n2", title="New Match", content="Student S3 has a 92% match with Ms. Elena Rodriguez.", type="Info")
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
