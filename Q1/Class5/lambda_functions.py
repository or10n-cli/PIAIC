# Lambda Functions

# Square Function
square = lambda a: a * a * a
# Usage
print(square(50)) # 125000

# Multiply Function
multiply = lambda a,b: a * b
# Usage
print(multiply(40, 50)) # 2000

# Positive & Negative Number Checker
chk_number = lambda a: "Positive" if a > 0 else "Negative" if a < 0 else "Zero"
# Usage
print(chk_number(10)) # Positive

# If a Number is Positive Checker
if_positive = lambda a: a >= 0
# Usage
print(if_positive(0)) # TRUE
