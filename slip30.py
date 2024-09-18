
class Country:

                def AcceptCountry(self):

                                self.cname=input("Enter Country Name: ")

                def DisplayCountry(self):

                                print("Country Name is:", self.cname)

 

class State(Country):

                def AcceptState(self):

                                self.sname=input("Enter State Name: ")

                def DisplayState(self):

                                print("State Name is:", self.sname)

#main body

Obj=State()

Obj.AcceptCountry()

Obj.AcceptState()

Obj.DisplayCountry()

Obj.DisplayState()
