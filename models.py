from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum

class RiskLevel(str, Enum):
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    RED = "Red"

class StudentProfile(BaseModel):
    id: str
    name: str
    # Academic
    gpa: float
    subject_performance: Dict[str, float]
    skill_gaps: List[str]
    # Behavioral
    engagement_frequency: int # Sessions per week
    responsiveness: float # 0-1
    communication_preference: str
    # Wellness
    stress_level: float # 0-100
    sleep_patterns: float # Hours
    wellbeing_score: float # 0-100
    # Productivity
    task_completion_rate: float # 0-1
    time_management_indicator: float # 0-100
    # Career
    goal_clarity: float # 0-100
    skill_alignment: float # 0-100
    readiness_timeline: int # Months to graduation

class MentorProfile(BaseModel):
    id: str
    name: str
    domain_expertise: List[str]
    experience_level: int # Years
    mentoring_style: str
    availability: float # Hours per week
    support_capacity: int # Number of students
    historical_effectiveness: float # 0-100

class ScoringResult(BaseModel):
    student_id: str
    aps: float # Academic Performance Score
    wws: float # Wellness & Wellbeing Score
    ptms: float # Productivity & Time Management Score
    crs: float # Career Readiness Score
    sri: float # Student Readiness Index
    risk_level: RiskLevel

class MentorMatch(BaseModel):
    mentor_id: str
    mentor_name: str
    similarity_score: float
    matching_features: List[str]

class SRICalculationInput(BaseModel):
    gpa: float
    subject_avg: float
    wellbeing: float
    stress: float
    sleep: float
    tasks: float
    mgt: float
    goals: float
    alignment: float
    timeline: int

class ChatMessage(BaseModel):
    id: str
    sender_id: str
    sender_name: str
    content: str
    timestamp: str

class Notification(BaseModel):
    id: str
    title: str
    content: str
    type: str # Info, Warning, Alert
    read: bool = False
