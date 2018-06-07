print("Hello world!")
print(1+1)
print(2*9)
print(3**9)

name = input("What is your name?")
print("Your name is", name)

print(3**150)
print(pow(3,150))

import math
math.pi
import random
random.random()

 cc='''это очень большая
... строка, многострочный
... блок текста'''

 print(cc)

c = [c * 3 for c in 'list']






l = [str(i)+str(i-1) for i in range(20)]
f = open('text.txt', 'w')
for index in l:
   f.write(index + '\n')

f.close()

f = open('text.txt', 'r')
l = [line.strip() for line in f]



l = [str(i)+str(i-1) for i in range(20)]
with open('text.txt', 'w') as f:
    for index in l:
        f.write(index + '\n')
