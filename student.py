
class StudentProfile:
    def __init__(self,student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.__total_score = 0
    
    def add_points(self,points_earned:int):
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")
            
        self.__total_score += points_earned
        print(f"{points_earned} points added to your inventory!")
    def get_current_score(self):
        return self.__total_score
