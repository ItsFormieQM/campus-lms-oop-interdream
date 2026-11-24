# this has translation ig
import localizer
class StudentProfile:
    def __init__(self,student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.__total_score = 0
    
    def add_points(self,points_earned):
        if points_earned < 0:
            raise ValueError(localizer.text_setloc("Cannot add negative points!","error_msg1"))
            
        self.__total_score += points_earned
        print(f"{points_earned}{localizer.text_setloc(" points added to your inventory!","success_msg1")}")
    def get_current_points(self):
        return self.__total_score

test = StudentProfile("Former","67")
test.add_points(0)