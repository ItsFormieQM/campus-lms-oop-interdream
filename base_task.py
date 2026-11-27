from abc import ABC, abstractmethod

class AcademicTask(ABC): 
    @abstractmethod
    def __init__(self, title: str, max_points: int):
        self.title = title
        self.max_points = max_points
        self.is_graded = False

    def submit_work(self):
        pass

    def grade_work(self):
        pass

    def get_details(self):
        pass 