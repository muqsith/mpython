print(1/0.5)

while True:
    try:
        x = int(input('Please enter a number\n'))
        break
    except ValueError:
        print('Try again')