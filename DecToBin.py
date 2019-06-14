passString = ""
state = 0
output = ""
import time


def nextstate(pas):
    global output
    global passString
    temp = ""
    global state
    state = 0
    for each in pas:
        if each == "0" and state == 0:
            temp += "0"
            state = 0
        elif each == "1" and state == 0:
            temp += "0"
            state = 1
        elif each == "2" and state == 0:
            temp += "1"
            state = 0
        elif each == "3" and state == 0:
            temp += "1"
            state = 1
        elif each == "4" and state == 0:
            temp += "2"
            state = 0
        elif each == "5" and state == 0:
            temp += "2"
            state = 1
        elif each == "6" and state == 0:
            temp += "3"
            state = 0
        elif each == "7" and state == 0:
            temp += "3"
            state = 1
        elif each == "8" and state == 0:
            temp += "4"
            state = 0
        elif each == "9" and state == 0:
            state = 1
            temp += "4"

        elif each == "0" and state == 1:
            temp += "5"
            state = 0
        elif each == "1" and state == 1:
            temp += "5"
            state = 1
        elif each == "2" and state == 1:
            temp += "6"
            state = 0
        elif each == "3" and state == 1:
            temp += "6"
            state = 1
        elif each == "4" and state == 1:
            temp += "7"
            state = 0
        elif each == "5" and state == 1:
            temp += "7"
            state = 1
        elif each == "6" and state == 1:
            temp += "8"
            state = 0
        elif each == "7" and state == 1:
            temp += "8"
            state = 1
        elif each == "8" and state == 1:
            temp += "9"
            state = 0
        elif each == "9" and state == 1:
            temp += "9"
            state = 1

    if int(temp) % 2 == 0:
        output += "0"
    else:
        output += "1"
    passString = temp
    return temp


if __name__ == '__main__':

    decision = 1
    while decision != 0:
        output = ""
        passString = input("Enter the decimal number to be converted into Binary.\n")
        l = passString
        for _ in range(4 * len(l)):
            passString = nextstate(passString)
        output = output[::-1]
        if int(l) % 2 == 0:
            output += "0"
        elif int(l) % 2 == 1:
            output += "1"

        print("Binary Equivalent: " + output)
        #  time.sleep(5000)
        decision = int(input("Press 1 to convert another decimal number\nPress 0 to Exit.\n"))

# time.sleep(5000)
