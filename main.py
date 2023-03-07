for num in range(1, 101):
    text = ""

    if (num % 3 == 0): text += "Fizz"
    if (num % 5 == 0): text += "Buzz"

    print(text if text != "" else str(num))