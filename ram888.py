# wap desing a menu and sub menus on the console


import os


def mastermenu():
    os.system("cls")
    ans=0
    print("\n\n\n\n\n")
    print("\t\t\t\t 1-general programs")
    print("\t\t\t\t 2-system control")
    print("\t\t\t\t 3-open applications")
    print("\t\t\t\t 4-exit")

    ans=int(input("\t\t\t choose your choice"))
    if(ans==1):
        general()
    elif(ans==2):
        control()
    elif(ans==3):
        openapps()
    else:
        print("bye..bye..")

#----general menu

def general():
    os.system("cls")
    ans=0
    print("\n\n\n\n\n")
    print("\t\t\t\t 1-good morning")
    print("\t\t\t\t 2-good afternoon")
    print("\t\t\t\t 3-good night")
    print("\t\t\t\t 0-go home")

    ans=int(input("\t\t\t choose your choice"))
    if(ans==1):
        gm()
    elif(ans==2):
        ge()
    elif(ans==3):
        gn()
    else:
        mastermenu()

#----start to design functions

def gm():
    print("good morning")
    input()
    general()
def ge():
    print("good evening")
    input()
    general()
def gn():
    print("good night")
    input()
    general()
    mastermenu()

def control():
    os.system("cls")
    ans=0
    print("\n\n\n\n\n")
    print("\t\t\t\t 1-shutdown")
    print("\t\t\t\t 2-restart")
    print("\t\t\t\t 0-go home")

    ans=int(input("\t\t\t choose your choice"))
    if(ans==1):
        shutdown()
    elif(ans==2):
        restart()
    else:
        mastermenu()

        
def shutdown():
    import os
    opt=input("want to shutdown yourcomputer:Y/n")
    if opt=='Y'or opt=='y':
        os.system("shutdown /s /t 10")
    else:
        print("continue your work..")
        mastermenu()
def restart():
    import os
    opt=input("want to shutdown yourcomputer:Y/n")
    if opt=='Y'or opt=='y':
        os.system("shutdown /r /t 10")
    else:
        print("continue your work..")
        mastermenu()

def openapps():
    os.system("cls")
    ans=0
    print("\n\n\n\n\n")
    print("\t\t\t\t 1-calculator")
    print("\t\t\t\t 2-notepad")
    print("\t\t\t\t 3-mspaint")
    print("\t\t\t\t 0-go home")

    ans=int(input("\t\t\t choose your choice"))
    if(ans==1):
        calculator()
    elif(ans==2):
        notepad()
    elif(ans==3):
        mspaint()
    else:

     mastermenu()      
def calculator():
    import os
    os.system("calculator")
def mspaint():
    import os
    os.system("mspaint")
def notepad():
    import os
    os.system("notepad")
mastermenu()
