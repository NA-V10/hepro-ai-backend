from models import StudentProfile, MentorProfile


# =========================
# STUDENTS
# =========================

def seed_students(db):
    """
    Seed demo students S1–S10
    """

    for i in range(1, 11):
        sid = f"S{i}"

        db[sid] = StudentProfile(
            id=sid,
            name=f"Student {i}",

            # academics
            gpa=round(3.0 + (i * 0.05), 2),
            subject_performance={"avg": 70 + i * 2},

            # behavior
            skill_gaps=[],
            engagement_frequency=3,
            responsiveness=0.8,
            communication_preference="Auto",

            # wellbeing
            stress_level=20 + i * 3,
            sleep_patterns=7,
            wellbeing_score=75 + i,

            # productivity
            task_completion_rate=round(0.7 + (i * 0.02), 2),
            time_management_indicator=70 + i,
            goal_clarity=75 + i,
            skill_alignment=80,

            readiness_timeline=12
        )

    print("✅ Seeded students")


# =========================
# MENTORS
# =========================

def seed_mentors(db):
    """
    Seed demo mentors
    """

    db["M1"] = MentorProfile(
        id="M1",
        name="Dr. Sarah Johnson",
        expertise=["AI", "ML", "Career Guidance"],
        capacity=10
    )

    db["M2"] = MentorProfile(
        id="M2",
        name="Prof. David Miller",
        expertise=["DSA", "Systems", "Problem Solving"],
        capacity=8
    )

    db["M3"] = MentorProfile(
        id="M3",
        name="Ms. Elena Rodriguez",
        expertise=["Wellness", "Soft Skills", "Productivity"],
        capacity=6
    )

    print("✅ Seeded mentors")
