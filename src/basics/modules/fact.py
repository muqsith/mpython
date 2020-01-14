import sys

MMZNUMBER = 3.583049

def fact(n):
    result = 1
    while (n > 0):
        result *= n
        n -= 1
    return result

def fib(n):
    a, b = 0, 1
    result = []
    while (n > 0):
        result.append(a)
        a, b = b, a+b
        n -= 1
    return result


if __name__ == '__main__':
    fn = ''
    n = 1
    if len(sys.argv) > 1:
        fn = sys.argv[1]
        n = int(sys.argv[2])
    if fn == 'factorial':
        print(fact(n))
    else:
        result = fib(n)
        print(n, 'element(s) of Fibonacci series')
        for i in result:
            print(i)