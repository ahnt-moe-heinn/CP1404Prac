def print_fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(0, n):
        print(n1, end="")
        n3 = n1+n2
        n1 = n2
        n2 = n3
    print()

def recursion_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)