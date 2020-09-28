# FizzBuzz Exercise

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0: # if a number is both divisible by:
        print("FizzBuzz")
        continue
    elif num % 3 ==0:
        print("FizzBuzz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue
    print(num)
