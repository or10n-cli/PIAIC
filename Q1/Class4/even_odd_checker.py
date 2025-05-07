# A custom function to check if a number is even or odd
def even_odd_checker(num):
    if num % 2 == 0:
        print("This is an Even Number.")
    else:
        print("This is an Odd Number.")
    return num

even_odd_checker(int(input("Enter a Number: ")))