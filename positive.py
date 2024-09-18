try:
    num=int(input('Enter a number :'))
except ValueError:
    print("\nThis is a positive number!")
else:
    print('\nnumber is  negative: ',num)
