# Exercise 1 - turn the shopping cart program from yesterday into an object-oriented program
# create a class called cart that retains items and has methods to add , remove and show 

class Cart():
    '''
    Shopping Cart will have below attributes:
    - items
    - checkout 

    '''
    def __init__(self, ordertotal, items = [], savedlist = []):  #should items is a list or dictionary but dictionary only have (key, value)
        self.ordertotal = ordertotal
        self.items = items
        self.savedlist = savedlist
        
    def GoCheckOut(self):
        if len(self.items) == 0:
            print("Your cart is empty. Thank you for visiting Dollor Store! ")
        else:
            print(f"Thank you for shopping in Dollar Store! Your total is ${len(self.items)}. ")
    
    def CheckOutBeforeQuit(self):
        if len(self.items) > 0:
            reminder = input("You left something in your cart, do you want to check out first?")
            if reminder == 'yes':
                print(f"Thank you for shopping in Dollar Store! Your total is ${len(self.items)}. ")
            else:
                print("Thank you for visiting Dollor Store! ")
            
    def ShowCart(self):
        if len(self.items) == 0:
            print("Your cart is empty. ")
        else:
            print("---Shopping Cart---")
            for item in self.items:
                print(item)
    
    def AddItemIntoCart(self):
        AddItem = input("What would you like to add? ")
        self.items.append(AddItem)


    def RemoveIteminCart(self):
        print(f"---Shopping Cart----\n {self.items}")
        deleteItem = input("Which item would you like to delete? ")
        self.items.remove(deleteItem)
    
    
    def SavedList(self):
        #from SavedList import savedForLater
        self.savedlist = ['mug']
        print(f"You saved {self.savedlist} for later. ")
        moveToChart = input("What product would you like to move to cart now? ")

        self.savedlist.remove(moveToChart) 
        print(f"{moveToChart} has been added to your cart now.")
        self.items.append(moveToChart)


        # if moveToChart not in self.savedlist:
        #     print("You only can enter the item in the saved list. ")
        # else:
        #     self.savedlist.remove(moveToChart) 
        #     print(f"{moveToChart} has been added to your cart now.")
        #     self.items.append(moveToChart)
            

        # if moveToChart in self.savedlist:
        #     self.savedlist.remove(moveToChart)
        #     self.items.append(moveToChart)
        #     print(f"{moveToChart} has been added to your cart now,")
        # else:
        #     print("You only can enter the item that saved in the saved list. ")

MyCart = Cart(2)

def run():
    while True:
        response = input("What would you like to add, remove, show or quit?")

        if response == 'quit':
            MyCart.ShowCart()
            MyCart.CheckOutBeforeQuit()
            break

        elif response == 'add':
            MyCart.AddItemIntoCart()

        elif response == 'remove':
            MyCart.RemoveIteminCart()

        elif response == 'show':
            selection = input("What would you like to see? \n- Items\n- Saved List\n- Order Total\n")
            if selection.lower() == 'saved list':
                MyCart.SavedList()
            elif selection.lower() == 'order total':
                MyCart.GoCheckOut()
            else:
                MyCart.ShowCart()
        
        else: 
            print("Ther is not a valid ption. Please enter add/ remove/ show/ quit.")

run()


# Exercise 2
# class String_Typing():

#     def __init__(self, get_string = ""):
#         self.get_string = get_string

#     def GetAns(self):
#         self.get_string = input("Type something here. ")
    
#     def PrintAns(self):
#         print("Ans in uppercase:", self.get_string.upper())


# string_typing_instance = String_Typing()

# string_typing_instance.GetAns()

# string_typing_instance.PrintAns()


