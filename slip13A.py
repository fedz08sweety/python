num = int (input("Enter Any Positive number:"))

try:

                if num >= 0:

                      raise ValueError("Positive Number-Input Number is Correct")

                else:

                      raise ValueError("Negative Number-Input Number is InCorrect")

except ValueError as e:

    print(e)