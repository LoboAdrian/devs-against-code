import os, time

black = ["What makes people feel power.", "How to impress your friends", "Something overrated."]

white = ["BTW I use Arch", "Blue switches sound", "Brainfuck", "C++ is a horrible language. Quite frankly, even if the choice of C were to do *nothing* but keep the C++ programmers out,that in itself would be a huge reason to use C."]

os.system('clear')

for i in range(len(black)):
    print("{}. {}".format(i, black[i]))
b = int(input("Choose one: "))
os.system('clear')
print(black[b] + "\n")

for i in range(len(white)):
    print("{}. {}".format(i, white[i]))
a = int(input("Choose one: "))
os.system('clear')
time.sleep(1)
print(black[b] + "\n" + white[a])
