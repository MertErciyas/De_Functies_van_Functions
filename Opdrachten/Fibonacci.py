num1 = 0
num2 = 1
num3 = 1
fibonaccilist = []

def fibonacci(times):
    for i in range(times):
        global num1;global num2;global num3
        num3 = num1 + num2
        fibonaccilist.append(num3)
        num1 = num2     
        num2 = num3
    return fibonaccilist

choice = int(input("How many spots would you like to see?\n"))
print("You're numbers are:", fibonacci(choice))
