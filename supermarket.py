from datetime import datetime
name=input("Enter your name:")
lists='''
Rice   Rs 20/kg
Sugar  Rs 30/kg
salt   Rs 20/kg
oil    Rs 80/litre
Panner Rs 100/kg
Maggi  Rs 50/kg
Boost  Rs 90/each
Colgate Rs 85/each'''
 
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for item
items={'rice':20,'sugar':30,'salt':20,'oil':80,'panner':100,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry, your entered item is not available")
    else:
        print("You entered wrong number")
    inp=input("can i bill the items yes or no: ")
    if inp=='yes':
        if finalamount!=0:
            print(25*"=","Sai supermarket",25*"=")
            print(28*" ","peddapuram")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("S.no",8*" ",'items',8*" ","Quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*" ",5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount: ",'Rs',totalprice)
            print("GstAmount: ",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")



  
