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
    s = None
    u = None
    v = None
    t = None
    knownsList = []
    remainingVars = []
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
        if len(knowns) == 2 and len(set(knowns)) == 2 and all(letter in valid_letters for letter in knowns):
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

    for letter in valid_letters:
        if letter not in knownsList:
            remainingVars.append(letter)
    while True:
        print("What variable is unknown")
        wait(0.5)
        print("The remaining variables are:", (remainingVars))
        unknown = input().lower()
        if len(unknown) == 1:
            if unknown in remainingVars:
                break
            print("Please pick a valid unkown")
        print("Please enter a valid input")
    knownsList.append(unknown)

    if "s" not in knownsList:
        if unknown == "u":
            u = v - (a*t)
        elif unknown == "v":
            v = u + (a*t)
        elif unknown == "t":
            t = (v-u)/a
    elif "u" not in knownsList:
        if unknown == "s":
            s = (v*t) - (0.5*a*(t**2))
        elif unknown == "v":
            v = (s/t) + (0.5*a*t)
        elif unknown == "t":
            A = (-0.5 * a)
            B = v
            C = -s
            if ((B**2)-(4*A*C)) < 0:
                print("The object does not reach this height")
                return
            else:
                t1 = (-B-(math.sqrt((B**2)-(4*A*C))))/(2*A)
                t2 = (-B+(math.sqrt((B**2)-(4*A*C))))/(2*A)
                if t1 > 0:
                    t = t1
                else:
                    t = t2
    elif "v" not in knownsList:
        if unknown == "s":
            s = (u*t) + (0.5*a*(t**2))
        elif unknown == "u":
            u = (s/t) - (0.5*a*t)
        elif unknown == "t":
            A = (0.5 * a)
            B = u
            C = -s
            if ((B**2)-(4*A*C)) < 0:
                print("The object does not reach this height")
                return
            else:
                t1 = (-B-(math.sqrt((B**2)-(4*A*C))))/(2*A)
                t2 = (-B+(math.sqrt((B**2)-(4*A*C))))/(2*A)
                if t1 > 0:
                    t = t1
                else:
                    t = t2
    elif "t" not in knownsList:
        if unknown == "s":
            s = ((v**2)-(u**2))/(2*a)
        elif unknown == "u":
            if ((v**2)-(2*a*s)) < 0:
                print("The object does not reach this height")
                return
            else:
                u = math.sqrt((v**2)-(2*a*s))
        elif unknown == "v":
            if ((u**2)+(2*a*s)) < 0:
                print("The object does not reach this height")
                return
            else:
                v = math.sqrt((u**2)+(2*a*s))

    if unknown == "s" and s!=None:
        print(f"The displacement is {s}m")
    elif unknown == "u" and u!=None:
        print(f"The initial velocity is {u}m/s")
    elif unknown == "v" and v!=None:
        print(f"The final velocity is {v}m/s")
    elif unknown == "t" and t!=None:
        print(f"The time taken is {t}s")
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
