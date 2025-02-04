# very simple program to find if the number is prime or not


def prime():
    num = int(input("enter the number \n"))
    if num == 1:
         return "Prime should be greater then 1"
    for i in range(2, num): 
        if num % i == 0:
             return "not prime"
        else:
             return "is prime"
        
print(prime())
    