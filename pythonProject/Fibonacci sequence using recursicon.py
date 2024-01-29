# Python programme to slove the fibonacci sequence using recursicon

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
    print (fib(7))
