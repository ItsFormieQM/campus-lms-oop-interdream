from base_task import AcademicTask
from abc import abstractmethod, ABC

class Quiz(AcademicTask):
    def __init__(self, total_questions:str, max_points: int):
        super().__init__(self, title, max_points)
