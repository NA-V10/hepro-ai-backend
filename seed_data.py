import requests
import random

BASE_URL = "http://localhost:8000"

def create_mock_data():
    # Create Mentors
    mentors = [
        {
            "id": "M1",
            "name": "Dr. Sarah Johnson",
            "domain_expertise": ["Computer Science", "AI/ML"],
            "experience_level": 12,
            "mentoring_style": "Proactive",
            "availability": 5.0,
            "support_capacity": 5,
            "historical_effectiveness": 95.0
        },
        {
            "id": "M2",
            "name": "Prof. David Miller",
            "domain_expertise": ["Data Science", "Statistics"],
            "experience_level": 15,
            "mentoring_style": "Supportive",
            "availability": 3.0,
            "support_capacity": 3,
            "historical_effectiveness": 88.0
        },
        {
            "id": "M3",
            "name": "Ms. Elena Rodriguez",
            "domain_expertise": ["Software Engineering", "Career Coaching"],
            "experience_level": 8,
            "mentoring_style": "Direct",
            "availability": 10.0,
            "support_capacity": 10,
            "historical_effectiveness": 92.0
        },
        {
            "id": "M4",
            "name": "Dr. James Wilson",
            "domain_expertise": ["Cybersecurity", "Ethics"],
            "experience_level": 10,
            "mentoring_style": "Detail-oriented",
            "availability": 4.0,
            "support_capacity": 4,
            "historical_effectiveness": 90.0
        },
        {
            "id": "M5",
            "name": "Prof. Linda Taylor",
            "domain_expertise": ["Human-Computer Interaction", "Design"],
            "experience_level": 20,
            "mentoring_style": "Creative",
            "availability": 2.0,
            "support_capacity": 2,
            "historical_effectiveness": 98.0
        }
    ]

    for m in mentors:
        requests.post(f"{BASE_URL}/mentors/", json=m)

    # Create Students
    students = [
        {
            "id": "S1",
            "name": "Alice Chen",
            "gpa": 3.8,
            "subject_performance": {"Math": 95, "CS": 98, "Physics": 88},
            "skill_gaps": ["Communication"],
            "engagement_frequency": 4,
            "responsiveness": 0.9,
            "communication_preference": "Slack",
            "stress_level": 20,
            "sleep_patterns": 7.5,
            "wellbeing_score": 85,
            "task_completion_rate": 0.95,
            "time_management_indicator": 90,
            "goal_clarity": 95,
            "skill_alignment": 90,
            "readiness_timeline": 12
        },
        {
            "id": "S2",
            "name": "Bob Smith",
            "gpa": 2.5,
            "subject_performance": {"Math": 65, "CS": 70, "Physics": 60},
            "skill_gaps": ["Problem Solving", "Coding"],
            "engagement_frequency": 1,
            "responsiveness": 0.4,
            "communication_preference": "Email",
            "stress_level": 80,
            "sleep_patterns": 5.0,
            "wellbeing_score": 40,
            "task_completion_rate": 0.5,
            "time_management_indicator": 40,
            "goal_clarity": 30,
            "skill_alignment": 40,
            "readiness_timeline": 24
        },
        {
            "id": "S3",
            "name": "Charlie Davis",
            "gpa": 3.2,
            "subject_performance": {"Math": 80, "CS": 85, "Physics": 75},
            "skill_gaps": ["Public Speaking"],
            "engagement_frequency": 3,
            "responsiveness": 0.7,
            "communication_preference": "In-person",
            "stress_level": 50,
            "sleep_patterns": 6.5,
            "wellbeing_score": 70,
            "task_completion_rate": 0.8,
            "time_management_indicator": 70,
            "goal_clarity": 70,
            "skill_alignment": 80,
            "readiness_timeline": 18
        },
        {
            "id": "S4",
            "name": "Diana Prince",
            "gpa": 3.9,
            "subject_performance": {"Math": 98, "CS": 100, "Physics": 95},
            "skill_gaps": [],
            "engagement_frequency": 5,
            "responsiveness": 1.0,
            "communication_preference": "Discord",
            "stress_level": 10,
            "sleep_patterns": 8.0,
            "wellbeing_score": 95,
            "task_completion_rate": 1.0,
            "time_management_indicator": 95,
            "goal_clarity": 100,
            "skill_alignment": 95,
            "readiness_timeline": 6
        },
        {
            "id": "S5",
            "name": "Evan Wright",
            "gpa": 2.1,
            "subject_performance": {"Math": 50, "CS": 45, "Physics": 55},
            "skill_gaps": ["Study Skills", "Focus"],
            "engagement_frequency": 0,
            "responsiveness": 0.2,
            "communication_preference": "Phone",
            "stress_level": 90,
            "sleep_patterns": 4.0,
            "wellbeing_score": 30,
            "task_completion_rate": 0.3,
            "time_management_indicator": 20,
            "goal_clarity": 10,
            "skill_alignment": 20,
            "readiness_timeline": 36
        },
        {
            "id": "S6",
            "name": "Fiona Gallagher",
            "gpa": 3.6,
            "subject_performance": {"Math": 88, "CS": 92, "Physics": 85},
            "skill_gaps": ["Leadership"],
            "engagement_frequency": 4,
            "responsiveness": 0.8,
            "communication_preference": "Slack",
            "stress_level": 30,
            "sleep_patterns": 7.0,
            "wellbeing_score": 80,
            "task_completion_rate": 0.9,
            "time_management_indicator": 85,
            "goal_clarity": 90,
            "skill_alignment": 85,
            "readiness_timeline": 12
        },
        {
            "id": "S7",
            "name": "George Miller",
            "gpa": 2.8,
            "subject_performance": {"Math": 70, "CS": 65, "Physics": 72},
            "skill_gaps": ["Time Management"],
            "engagement_frequency": 2,
            "responsiveness": 0.5,
            "communication_preference": "Email",
            "stress_level": 60,
            "sleep_patterns": 6.0,
            "wellbeing_score": 55,
            "task_completion_rate": 0.6,
            "time_management_indicator": 50,
            "goal_clarity": 40,
            "skill_alignment": 55,
            "readiness_timeline": 24
        },
        {
            "id": "S8",
            "name": "Hannah Abbott",
            "gpa": 3.4,
            "subject_performance": {"Math": 82, "CS": 80, "Physics": 85},
            "skill_gaps": ["Public Speaking"],
            "engagement_frequency": 3,
            "responsiveness": 0.7,
            "communication_preference": "Discord",
            "stress_level": 40,
            "sleep_patterns": 6.5,
            "wellbeing_score": 75,
            "task_completion_rate": 0.85,
            "time_management_indicator": 75,
            "goal_clarity": 80,
            "skill_alignment": 75,
            "readiness_timeline": 18
        },
        {
            "id": "S9",
            "name": "Ian Somerhalder",
            "gpa": 3.9,
            "subject_performance": {"Math": 95, "CS": 98, "Physics": 92},
            "skill_gaps": [],
            "engagement_frequency": 5,
            "responsiveness": 1.0,
            "communication_preference": "Slack",
            "stress_level": 15,
            "sleep_patterns": 8.0,
            "wellbeing_score": 90,
            "task_completion_rate": 0.98,
            "time_management_indicator": 95,
            "goal_clarity": 95,
            "skill_alignment": 98,
            "readiness_timeline": 6
        },
        {
            "id": "S10",
            "name": "Jane Eyre",
            "gpa": 2.3,
            "subject_performance": {"Math": 55, "CS": 50, "Physics": 60},
            "skill_gaps": ["Math", "Physics"],
            "engagement_frequency": 1,
            "responsiveness": 0.3,
            "communication_preference": "Email",
            "stress_level": 75,
            "sleep_patterns": 5.5,
            "wellbeing_score": 45,
            "task_completion_rate": 0.45,
            "time_management_indicator": 35,
            "goal_clarity": 25,
            "skill_alignment": 35,
            "readiness_timeline": 30
        }
    ]

    for s in students:
        requests.post(f"{BASE_URL}/students/", json=s)

    print("Mock data created successfully!")

if __name__ == "__main__":
    try:
        create_mock_data()
    except Exception as e:
        print(f"Failed to create mock data: {e}. Is the server running?")
