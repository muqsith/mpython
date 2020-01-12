import math

def nums():
    print("Numeric operations ")
    print('2+2 = ', 2+2)
    print('50  - 5*6 = ', 50  - 5*6)
    print('17/3 = ', 17/3)
    print('17//3 = ', 17//3)
    print('17%3 = ', 17%3)
    print('2**2 = ', 2**2)
    print('4**0.5 = ', 4**0.5)
    print('2**0.5 = ', 2**0.5)

    length = 17
    width = 3
    print('Area(lxb): ', length * width, ' mt.sq')

    print("Euler's number (e): ", (1 + (1/100000)) ** 100000 )
    print("Complex numbers (2+3i): ", (2+3j) * 20)
    print("PI: ", math.pi)


def strs():
    print(r'C:\User\name\Desktop is path to desktop')
    print('''\n
    Play snake game in python
        keys: 
            <-  move left
            ->  move right
            v   move down
            ^   move up
    Enoy !!!!!!!!!
    ''')
    print('Py' 'thon')
    print('Py' + 'thon')
    print('Mi' + 'ssi' * 2 + 'p' * 2 + 'i')

    text = ('Webshop is a web application'
        ' with persistence')
    print(text)

    word = 'Python'
    print(word[0])
    print(word[-6])
    print(word[1:3])
    print(word[:4])
    print(word[2:])

    print('length of text: ', len(text))
    print()


def listings():
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    squares_copy = squares[:]
    print(squares_copy[:5])
    # concatenate lists with '+' operator
    more_squares = squares_copy + [121, 144, 169, 196, 225]
    print(more_squares[6:])
    cubes = [1, 8, 27, 61]
    cubes[3] = 64
    cubes.append(125)
    print(cubes)
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    letters[2:5] = ['C', 'D', 'E']
    print(letters)
    # empty list
    letters[:] = []
    print(letters)
    # nested lists
    n = [[1, 2, 3, 4], squares, cubes]
    print(n)
    print()



# nums()
# strs()
listings()