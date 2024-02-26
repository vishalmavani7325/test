# class Fruit:
#     def __init__(self,stock):
#         self.stock=stock
#     def displayfruit(self):
#         print("Total Fruit Stock",self.stock)
#     def fruitPrice(self,q):
        
#         if q<=0:
#             print("enter the postive value or greater then zero")
#         if q>self.stock:
#             print("enter the value (less then stock)")
#         else:
#             print("total price",q*100)
#             print("total fruit",self.stock)
        
# while True:
#     obj=Fruit(100)
#     uc=input(''' 
#      1.Display Stock
#      2.Fruit Price
#      3.exit     ''')
    
#     if uc=='1':
#         obj.displayfruit()
#     elif uc=='2':
#         n=int(input("enter the qty...."))
#         obj.fruitPrice(n)
#     else:
#         break
    
    