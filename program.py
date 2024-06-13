def numbers(n):
    if n>0:
        numbers(n-1)
        print(n,end=" ")
n=int(input("enter number"))
numbers(n)
