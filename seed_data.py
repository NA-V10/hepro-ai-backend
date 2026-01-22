from models import StudentProfile, MentorProfile


# =====================================================
# STUDENTS
# =====================================================

def seed_students(db):
    """
    Seed 10 realistic demo students
    """

    for i in range(1, 11):
        sid = f"S{i}"

        db[sid] = StudentProfile(
            id=sid,
            name=f"Student {i}",

            # Academic
            gpa=round(3.0 + i * 0.05, 2),
            subject_performance={"avg": 70 + i * 2},
            skill_gaps=[],

            # Behavioral
            engagement_frequency=3,
            responsiveness=0.8,
            communication_preference="Auto",

            # Wellness
            stress_level=20 + i * 3,
            sleep_patterns=7,
            wellbeing_score=75 + i,

            # Productivity
            task_completion_rate=0.75,
            time_management_indicator=75 + i,

            # Career
            goal_clarity=80,
            skill_alignment=80,
            readiness_timeline=12
        )

    print("✅ Students seeded")


# =====================================================
# MENTORS (MATCHED EXACTLY TO YOUR MODEL)
# =====================================================

def seed_mentors(db):
    """
    Seed mentors matching MentorProfile exactly
    """

    db["M1"] = MentorProfile(
        id="M1",
        name="Dr. Sarah Johnson",
        domain_expertise=["AI", "Machine Learning", "Career Guidance"],
        experience_level=8,
        mentoring_style="Analytical",
        availability=30,
        support_capacity=10,
        historical_effectiveness=92
    )

    db["M2"] = MentorProfile(
        id="M2",
        name="Prof. David Miller",
        domain_expertise=["DSA", "Systems Design", "Problem Solving"],
        experience_level=12,
        mentoring_style="Technical",
        availability=25,
        support_capacity=8,
        historical_effectiveness=88
    )

    db["M3"] = MentorProfile(
        id="M3",
        name="Ms. Elena Rodriguez",
        domain_expertise=["Wellness", "Soft Skills", "Productivity"],
        experience_level=6,
        mentoring_style="Supportive",
        availability=20,
        support_capacity=6,
        historical_effectiveness=95
    )

    print("✅ Mentors seeded")
