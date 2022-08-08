def fizzbuzz():
    for num in range(1,1000):
        string = ""
        if num % 3 == 0:
            string = string + "Fizz"
        if num % 5 == 0:
            string = string + "Buzz"
        if num % 3 == 0 and num % 5 == 0:
            string = string + "FizzBuzz"
        print(string)