import localizer
import portal
import essay_task
# import quiz_task
# import essay_task
# import auto_grader
from globalvars import slownsteady
import student
from math import floor
langlist = [
    localizer.text_logic_setloc("English","","en.json"),
    localizer.text_logic_setloc("Bisaya/Cebuano","","ceb.json")
]
langind = 0
def wait():
    if slownsteady:
        input(f"\n{localizer.text_setloc("Waiting... Press Enter to continue!","wait_prompt")}")
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
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_score()}")
print(f"{localizer.text_setloc(f"Adding ","intro3_1")}{temp}{localizer.text_setloc(f" points to the student should print an error.","intro3_2")}") 
try:
    st1.add_points(temp)
except ValueError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_score()}")
wait()

print("\n"+localizer.text_setloc("--- Test 2: Scores should be clamped to 100 (it errors actually when the score is over 100) ---","intro5")+"\n")
temp = -999
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_score()}")
print(f"{temp} {localizer.text_setloc("points will be added to demonstrate the result.","intro6")}")
try:
    st1.add_points(temp)
except ValueError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
    pass
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_score()}")
wait()

print("\n"+localizer.text_setloc("--- Test 3: Ensuring variable 'total_score' is private. ---","intro7")+"\n")
print(localizer.text_setloc("Accessing the private variable...","intro8"))
try:
    print(st1.__total_score)
except AttributeError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
wait()

print("\n"+localizer.text_setloc("--- Test 4: Course Portal should bar submission after its locked. ---","intro9")+"\n")
print(localizer.text_setloc("Submitting Test Work...","intro10"))
port1 = portal.CoursePortal("Game Development Basics - Music Design")
port1.accept_submission(st1.student_name)
port1.lock_portal()
try:
    port1.accept_submission(st1.student_name)
except ValueError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
    pass

print(localizer.text_setloc("Thats all of this simple testing ground for Practical 1.","intro10_end"))
wait()
print("[Practical 2]")
print(localizer.text_setloc("[Info] - This part simulates the Finals","intro11"))
# be gone memory users
del st1,port1
import quiz_task
import auto_grader
def quizassign(lsq):
    for i in range(len(lsq)):
        
        lsq[i][0].submit_work(lsq[i][1])
def essayassign(lsq):
    for i in range(len(lsq)):
        
        lsq[i][0].submit_work(lsq[i][1])
quizzes = [
    quiz_task.Quiz("Pointers and Addresses",20,40),
    quiz_task.Quiz("All about memory",25,45),

    essay_task.Essay("Why is C/C++ so common in games and programs back then?",30,100),
    essay_task.Essay("What is Reverse Engineering?",50,125),
]
quizassign(
    [
        [
            quizzes[0], 36
        ],
        [
            quizzes[1], 41
        ]
    ]
)
essayassign(
    [
        [
            quizzes[2], quizzes[2].get_minimum_word_count()
        ],
        [
            quizzes[3], quizzes[3].get_minimum_word_count() / 2
        ]
    ]
)
st1 = student.StudentProfile("Noelle Holiday","id-1225")
port1 = portal.CoursePortal("Computer Science General Topics - C/C++ Basics")
bg1 = auto_grader.BatchGrader()

print(localizer.text_setloc("\n--- Test 1: Checking if the student can submit before the deadline. ---\n","intro12"))
print(localizer.text_setloc("Making the student submit work...","intro13"))
port1.accept_submission(st1.student_name)
print(localizer.text_setloc("Locking submission bin...","intro14"))
port1.lock_portal()
print(localizer.text_setloc("Making the student submit work...","intro13"))
try:
    port1.accept_submission(st1.student_name)
except ValueError as e:
    print(e)
    print(localizer.text_setloc("To prevent the test from ending early, the exception was caught by the try-except function block.","intro4"))
    pass
wait()


print(localizer.text_setloc("\n--- Test 2: Passing the mixed list along with StudentProfile into the grade processor. ---\n","intro15"))
print(localizer.text_setloc("Passing arguments 'quizzes: list' and 'st1: Student Instance' into BatchGrader.process_grades()...","intro16"))
print(f"{localizer.text_setloc(f"Current score for","intro1_1")} {st1.student_name}: {st1.get_current_score()}")
bg1.process_grades(quizzes,st1)
wait()
print()
print(localizer.text_setloc("And thats all for Practical 2. Thank you for reading this!","intro17"))

wait()