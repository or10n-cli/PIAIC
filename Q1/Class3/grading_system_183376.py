# This Program reveals your Grade by checking your Obtained Percentage

# This percentage variable gets input from User
percentage = int(input("How much Percentage You Scored?, Ans: "))

# Conditional Percentage Checking & Grading
if percentage > 100:
    print("Oops🤭! You Entered an Invalid Value")
elif percentage >= 90:
    print("Congrats🎉! You got A+")
elif percentage >= 80:
    print("Superb🎉! You got A")
elif percentage >= 70:
    print("Welldone🎊! You got B")
elif percentage >= 60:
    print("Keep it up! You got C")
elif percentage >= 40:
    print("You have to work Hard! You got D")
else:
    print("Failed☹️, but Don't give up!")
