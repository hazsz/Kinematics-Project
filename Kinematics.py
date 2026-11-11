import time
import math

def wait(seconds):
    time.sleep(seconds)

def askValue(var, Llimit = None, Ulimit = None):
    while True:
        print("What is the", var)
        try:
            val = float(input())
            if Llimit is not None and Ulimit is not None:
                if Llimit <= val <= Ulimit:
                    break
                else:
                    print(f"Please enter a number between {Llimit} and {Ulimit}")
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    return val

def verticalMotion():
    s = null
    u = null
    v = null
    t = null
    knownsList = []
    print("An object is being thrown from a particular height from a ledge with a particular velocity")
    wait(0.5)

    print("Is this simulation happening on Earth?")
    userA1 = input().strip().lower()
    if ("yes" in userA1) and ("no" not in userA1):
        a = -9.807
    elif ("yes" not in userA1) and ("no" in userA1):
        while True:
            print ("what is the (positive) value of gravity?")
            try:
                a = -abs(float(input()))
                break
            except ValueError:
                print("Invalid input please try again")

    print("Out of these variable, which 2 do you currently know?")
    wait(0.5)
    print("displacement (s), initial velocity (u), air time (t), final velocity(v)")
    valid_letters = ["s", "u", "t", "v"]
    while True:
        print("Please type the corresponding letters without spaces")
        knowns = input()
        if len(knowns) == 2 and all(letter in valid_letters for letter in knowns):
            break
        print("Please try again")
    if "s" in knowns:
        s = askValue("displacement")
        knownsList.append("s")
    if "u" in knowns:
        u = askValue("inital velocity")
        knownsList.append("u")
    if "t" in knowns:
        t = askValue("time", 0, math.inf)
        knownsList.append("t")
    if "v" in knowns:
        v = askValue("final velocity")
        knownsList.append("v")
    
    while True:
    `   print("What variable is unkown")
        wait(0.5)
        remainingVars = valid_letters[] - knownsList[]
        print("The remaining variables are:", (remainingVars))`

    return

def parabolicMotion():
    return

print("Welcome to the kinematics simulator")
while True:
    wait(0.5)
    print("Would you like to caculate for vertical motion or parabolic motion?")
    userA = input().strip().lower()
    if ("vertical" in userA) and ("parabolic" not in userA):
        verticalMotion()
    elif ("vertical" not in userA) and ("parabolic" in userA):
        parabolicMotion()
    else:
        print("invalid input")
