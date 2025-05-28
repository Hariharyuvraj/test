l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)

list=[10,20,30,40,50]
list.reverse()
print(list)

l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)

l1=[10,20,30,40,50]
l1.reverse()
print(l1)

l2=[9,8,7,6,5,4,3,2,1]
l2.reverse()
print(l2)

# function 1
def say_hello():
    print('hello!')
say_hello()

# function 2
def name():
    print("my name is yuvraj")
name()

# function 3
def nick(name):
    print("Hello,", name)
nick('pooja')
nick('Anuja')

# if i pass list into function it convert into the 'set'

def convert(l):
    return(set(l))
               
convert([1,2,3,4,5])