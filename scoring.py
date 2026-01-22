from models import StudentProfile, ScoringResult, RiskLevel

class ScoringEngine:
    @staticmethod
    def calculate_aps(student: StudentProfile) -> float:
        # GPA (4.0 scale) normalized to 100 + average subject performance
        gpa_score = (student.gpa / 4.0) * 100
        avg_subject = sum(student.subject_performance.values()) / len(student.subject_performance) if student.subject_performance else 0
        return (gpa_score * 0.6) + (avg_subject * 0.4)

    @staticmethod
    def calculate_wws(student: StudentProfile) -> float:
        # Wellness = Wellbeing score - stress penalty + sleep bonus
        stress_penalty = student.stress_level * 0.5
        sleep_score = min(100, (student.sleep_patterns / 8.0) * 100)
        return (student.wellbeing_score * 0.4) + (sleep_score * 0.4) - (stress_penalty * 0.2) + 20

    @staticmethod
    def calculate_ptms(student: StudentProfile) -> float:
        return (student.task_completion_rate * 70) + (student.time_management_indicator * 0.3)

    @staticmethod
    def calculate_crs(student: StudentProfile) -> float:
        return (student.goal_clarity * 0.4) + (student.skill_alignment * 0.4) + ((1 - min(1, student.readiness_timeline/48)) * 20)

    @staticmethod
    def determine_risk_level(sri: float) -> RiskLevel:
        if sri >= 80: return RiskLevel.GREEN
        if sri >= 60: return RiskLevel.BLUE
        if sri >= 40: return RiskLevel.YELLOW
        return RiskLevel.RED

    def score_student(self, student: StudentProfile) -> ScoringResult:
        aps = self.calculate_aps(student)
        wws = self.calculate_wws(student)
        ptms = self.calculate_ptms(student)
        crs = self.calculate_crs(student)
        
        # SRI = 0.30 APS + 0.25 WWS + 0.20 PTMS + 0.25 CRS
        sri = (0.30 * aps) + (0.25 * wws) + (0.20 * ptms) + (0.25 * crs)
        
        return ScoringResult(
            student_id=student.id,
            aps=round(aps, 2),
            wws=round(wws, 2),
            ptms=round(ptms, 2),
            crs=round(crs, 2),
            sri=round(sri, 2),
            risk_level=self.determine_risk_level(sri)
        )
