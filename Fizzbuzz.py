#User manual Inpute 
def fizz_buzz():
    while True:
        try: 
            user_input = int(input("Enter A number: "))
        except:
            continue
        break
    if user_input % 3 == 0:
        print("Fizz")
    elif user_input % 5 == 0:
        print("Buzz")
    elif user_input % 3 and 5 == 0:
        print("FizzBuzz")
    else:
        print(f'Your NUmber {user_input} is not FizzBuzz....')
        
#FizzBuzz Ready List
def Fizzbuzz_List():
        if (fizzbuzz % 3 == 0) and (fizzbuzz % 5 == 0):
            print("FizzBuzz", end="")
        if fizzbuzz % 3 == 0:
            print("Fizz", end="")
        if fizzbuzz % 5 == 0:
            print("Buzz", end="")
        for fizzbuzz in range(100):
             fizzbuzz+=1
             print(fizzbuzz)

#User manual Inpute 
fizz_buzz()

#FizzBuzz Ready List
Fizzbuzz_List()

