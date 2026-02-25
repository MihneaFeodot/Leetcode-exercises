def fibo(n):
    if n <= 1:
        return n
    
    oneBack = fibo(n-1)
    twoBack = fibo(n-2)
    
    return oneBack + twoBack


if __name__ == '__main__':
    print(fibo(10))