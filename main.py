import localizer
import portal
import quiz_task
import essay_task
import auto_grader
import student
from math import floor
langlist = [
    localizer.text_logic_setloc("English","","en.json"),
    localizer.text_logic_setloc("Bisaya/Cebuano","","ceb.json")
]
langind = 0
def check_lang(li):
    if li >= 0 and li < len(langlist):
        localizer.switch_lang(langlist[li][2])
        print(localizer.text_setloc("Language set to ","intro2")+langlist[li][0])
        return True
    else:
        print("Language not set, out of bounds")
        return False
print("---Languages---")
for i in range(len(langlist)):
    print(f"{i+1}. {langlist[i][0]}")
try:
    langind = floor(int(input(localizer.text_setloc("Enter language to use (optional, press enter without input to fallback to english): ","null"))))-1
    check_lang(floor(langind))
except ValueError:
    check_lang(-666)

print(" [Practical 1]\n")


print(localizer.text_setloc("--- Test 1: Checking if the program displays an error when the parameter is negative ---","intro1") + "\n")
st1 = student.StudentProfile("Kris Holiday Dreemurr", "id-1225")
st1.add_points(1225)
temp = -999999
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_points()}")
print(f"{localizer.text_setloc(f"Adding ","intro3_1")}{temp}{localizer.text_setloc(f" points to the student should print an error.","intro3_2")}") 
try:
    st1.add_points(temp)
except ValueError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_points()}")


print("\n"+localizer.text_setloc("--- Test 2: Scores should be clamped to 100 (it errors actually when the score is over 100) ---","intro5")+"\n")
temp = -999
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_points()}")
print(f"{temp} {localizer.text_setloc("points will be added to demonstrate the result.","intro6")}")
try:
    st1.add_points(temp)
except ValueError as e:
    print(e)
    pass
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_points()}")


print("\n"+localizer.text_setloc("--- Test 3: Ensuring variable 'total_score' is private. ---","intro7")+"\n")
print(localizer.text_setloc("Accessing the private variable...","intro8"))
try:
    print(st1.__total_score)
except AttributeError as e:
    print(e)


exit()
