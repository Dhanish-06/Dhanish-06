# divisible by 3 then fizz
#if divisible by 5 then buzz
# if divisible by both 3 & 5 then fizz buzz

def fizz_buzz():
    input1 = int(input("enter the num"))
    if input1 %3 == 0:
        return "Fizz"
    if input1 %5 == 0:
        return "Buzz"
    if input1 %3 == 0 and input1 %5 == 0:
        return "Fizz Buzz"
    
    return input1

print(fizz_buzz())