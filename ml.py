import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple
from models import StudentProfile, MentorProfile, ScoringResult, MentorMatch

class MLAssistant:
    def __init__(self):
        self.kmeans = KMeans(n_clusters=4, random_state=42)
        
    def segment_students(self, scoring_results: List[ScoringResult]) -> List[int]:
        if not scoring_results:
            return []
        
        # Features for clustering: APS, WWS, PTMS, CRS
        features = np.array([[r.aps, r.wws, r.ptms, r.crs] for r in scoring_results])
        
        # Scale features if necessary, but here they are already 0-100
        clusters = self.kmeans.fit_predict(features)
        return clusters.tolist()

    def match_mentor(self, student: StudentProfile, mentors: List[MentorProfile]) -> List[MentorMatch]:
        if not mentors:
            return []

        # Vectorize student for matching (Academic, Style, etc.)
        # Simplified vector: [GPA score, Readiness, Goal Clarity]
        student_vec = np.array([
            (student.gpa / 4.0) * 100,
            student.goal_clarity,
            student.skill_alignment
        ]).reshape(1, -1)

        matches = []
        for mentor in mentors:
            # Simplified mentor vector based on student dimensions
            # In a real app, this would involve NLP on expertise/style
            mentor_vec = np.array([
                mentor.historical_effectiveness,
                mentor.experience_level * 5, # Scale years
                mentor.availability * 10
            ]).reshape(1, -1)

            sim = cosine_similarity(student_vec, mentor_vec)[0][0]
            
            matches.append(MentorMatch(
                mentor_id=mentor.id,
                mentor_name=mentor.name,
                similarity_score=round(float(sim), 4),
                matching_features=["Domain Alignment", "Experience Match"]
            ))

        # Sort by similarity score descending
        matches.sort(key=lambda x: x.similarity_score, reverse=True)
        return matches[:3] # Return top 3
