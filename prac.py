import sys

def addTwoNumbers(x,y):
    return x + y


if __name__ == '__main__':
    a, b = map(int,sys.stdin.readline().split(' '))
    print(addTwoNumbers(a,b))
