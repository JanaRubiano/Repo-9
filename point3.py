'''
Given a base base and a natural number n as a power, return base^n using recursion.
'''
def power_recursive(base:float, n:int) -> float:
    if n == 0:
        return 1
    elif n == 1:
        return base
    else:
        return base * power_recursive(base, n-1)
    
if __name__ == '__main__':
    base = float(input("Enter the base of a power: "))
    n = float(input("Enter an exponential: "))
    answer = power_recursive(base, n)
    print(answer)