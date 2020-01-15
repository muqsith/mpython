import sys

size = 'BIG'
color = 'BLUE'

def showSize():
    size = 'SMALL'
    global color
    color = 'RED'
    print('inner size', size)
    print('global color', color)

def changeSizeUsingModule():
    current_module = sys.modules[__name__]
    current_module.size = 'SMALL'
    print('2nd inner size', size)

print('Outer size before call', size)
print('Outer color before call', color)
showSize()
print('Outer size after call', size)
print('Outer color after call', color)
changeSizeUsingModule()
print('Outer size after 2nd call', size)



def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


def myfunc3():
    x = 2
    def myfunc4():
        nonlocal x
        x += 1
        print('value of x ', x)
    return myfunc4

f4 = myfunc3()
f4()
f4()
