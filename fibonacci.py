def fib(n):
    a=1
    b=1
    if n==1:
        print('o')
    elif n==2:
        print('0,1')
    else:
        print("the series is:")
        print('0',a,b,end=' ')
        for i in range(n-3):
            total=a+b
            b=a
            a=total
            print(total,end=' ')
        print()
        
