class MyClass:

    def Get_String(self):

        self.myStr=input("Enter any String: ")

    def Reverse_String(self):

        s=self.myStr

        cnt=len(s)

        i=cnt-1

        revStr=""

        while(i >= 0):

            revStr=revStr + s[i]

            i=i-1

            print("String in Reverse:" , revStr)

           

# main body

Obj=MyClass()

Obj.Get_String()

Obj.Reverse_String()