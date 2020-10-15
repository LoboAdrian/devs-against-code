import os, time

black = ["What makes people feel power.", "How to impress your friends", "Something overrated."]

white = ["BTW I use Arch", "Blue switches sound", "Brainfuck", "C++ is a horrible language. Quite frankly, even if the choice of C were to do *nothing* but keep the C++ programmers out,that in itself would be a huge reason to use C."]

os.system('clear')

b = int(input("1. {} \n2. {} \n3. {} \nChoose any: ".format(black[0], black[1], black[2])))
os.system('clear')
print(black[b - 1] + "\n")

a = int(input("1. {} \n2. {} \n3. {} \nChoose any: ".format(white[0], white[1], white[2])))
os.system('clear')
time.sleep(3)
print(black[b - 1] + "\n" + white[a - 1])
