import random; import time

#VARIABLE BANK START
choices = ["Heads", "Tails"]
ChoicesG = ["", "", "", ""]
#VARIABLE BANK END

def inch(mm):
    x = mm * 25.4
    print(f"{mm}mm = ",x,"in", sep="")

def mm(inch):
    b = inch / 25.4
    print(f"{inch}in = ",b,"in", sep="")

def coinflip(times):
    time.sleep()
    for i in range(times):
        print(random.choice(choices), sep="\n")

def choice(ChoiceA, ChoiceB, ChoiceC, ChoiceD):
    ChoicesG = {ChoiceA}, {ChoiceB}, {ChoiceC}, {ChoiceD}
    print(random.choice(ChoicesG))