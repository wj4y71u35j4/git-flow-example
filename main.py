from calculator import add, subtract

def main():
    print("SimpleCalc")
    a = 5
    b = 3
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")

if __name__ == "__main__":
    main()
