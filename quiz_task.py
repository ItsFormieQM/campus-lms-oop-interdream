import base_task

class Quiz(base_task.AcademicTask):
    def __init__(self, title, total_questions, max_points):
        super().__init__(title, max_points)
        self.__total_quetions = total_questions
        self.correct_answers = 0

    def submit_work(self, correct_answers):
        self.correct_answers = correct_answers
        print(f"Quiz submitted: {self.title}")

    def grade_work(self):
        self.is_graded = True 
        return ((self.correct_answers/self.__total_quetions)* self.max_points)

    def get_details(self):
        print(f"[QUIZ] {self.title} - Max Points: {self.max_points}")


