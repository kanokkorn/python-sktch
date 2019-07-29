#!/usr/bin/python3

def odd_even(x):
        if (x % 2) == 0:
                return print("This is even number")
        else:
                return print("This is odd number")

if __name__ == "__main__":

        odd_even(int(input("Enter number : ")))
        
