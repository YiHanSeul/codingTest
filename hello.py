from cmd import PROMPT
from unittest import result

## finalTest
a=3
if a>1:
    print("a는 1보다 크다")
### test

for b in [1,2,3]:
    print(b)

print("while문")
i=0
while i<3:
    i=i+1
    print(i)

print("함수연습")
def add(a,b):  
    return a+b
print(add(3,4))
'''
    이거  주석입니다
'''

food='"payhon is ver easy" \nhe says'
print(food)

a="apple"
print(a*2)

print(a[0:2])

print ("i eat %d apples" %3)

print("i eat fruits %s %d" %(a,3))

print("I eat {0} apples".format("five"))

print("{0:=^10}".format("hi2"))
print(a.upper())

print(a.replace("apple","banana"))

print(id(a))

a,b=("java","js")
print(id(a))
print(id(b))


'''prompt="""
1.add
2.del
3.list
4.quit
enter number:
"""
number =0
while number !=4:
     print(prompt)
     number=int(input())

def say():
    print("hi")
test=say()
'''


def test1(*number):
    result =0
    for a in number:
        result=result+a
    return result

print(test1())


def add_and_mul(a,b):
    return a+b,a*b

result,result1=add_and_mul(1,2)
print(result)


f=open("새파일.txt",'w')