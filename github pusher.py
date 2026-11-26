import os
# they dont know how to use git add and the rest so i had to make a program for ts son.. - Formerhyde / Pollux
try:
    os.system("git fetch --all")
    branch = input("Enter Branch Name: ")
    os.system(f"git switch {branch}")
    os.system("git add .")
    msg = input("Enter commit message (leave blank and press enter to Default): ")
    if msg:
        os.system(f"git commit -m \"{msg}\"")
    else:
        os.system("git commit -m \"No commit message.\"")
    os.system("git push")
except Exception:
    print("Issue, idk wtf is this")
