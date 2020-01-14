import math
def softmax(L):
    x = 0
    for i in range(len(L)+1):
        x += pow(math.e, i)
    return pow(math.e, len(L)) / x

if __name__ == '__main__':
    ans = input('enter number: ')
    print(softmax(ans))
