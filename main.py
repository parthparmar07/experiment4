# main.py - Simple Calculator Application

from add import add
from sub import sub
from mul import mul

def main():
    print("Simple Calculator")
    a = 10
    b = 5
    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {sub(a, b)}")
    print(f"Multiplication: {a} * {b} = {mul(a, b)}")
    # Minor enhancement: Add a welcome message

if __name__ == "__main__":
    main()