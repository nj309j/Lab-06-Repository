def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    num1 = int(input("Please input your first number: "))
    num2 = int(input("Please input your second number: "))
    sum = add(num1, num2)
    difference = subtract(num1, num2)
    print(f"{num1} + {num2} = {sum}")
    print(f"{num1} + {num2} = {difference}")
