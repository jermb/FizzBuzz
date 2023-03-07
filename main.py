for num in range(1, 101):                   #   Loops through all number from 1 to 100
    text = ""                               #   Creates an empty string to push text into

    if (num % 3 == 0): text += "Fizz"       #   Check if number is divisible by 3: Add Fizz to string
    if (num % 5 == 0): text += "Buzz"       #   Check if divisible by 5: Add Buzz
                                            #   If divisible by 3 & 5 string will = "FizzBuzz"

    print(text if text != "" else str(num)) #   If text is not empty (Fizz and/or Buzz have been added) Prints the text string
                                            #   Otherwise prints the current number