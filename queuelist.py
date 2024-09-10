# Implement Queue using List(Functions)

q=[]

def Insert():

    if len(q)==size: # check wether the stack is full or not

        print("Queue is Full!!!!")

    else:

        element=input("Enter the element:")

        q.append(element)

        print(element,"is added to the Queue!")

def Delete():

    if len(q)==0:

        print("Queue is Empty!!!")

    else:

        e=q.pop(0)

        print("element removed!!:",e)

def display():

    print(q)

#Main body

size=int(input("Enter the size of Queue:"))

while True:

    print("\nSelect the Operation: 1.Insert 2.Delete 3.Display 4.Quit")

    choice=int(input())

    if choice==1:

        Insert()

    elif choice==2:

        Delete()

    elif choice==3:

        display()

    elif choice==4:

        break

    else:

        print("Invalid Option!!!")