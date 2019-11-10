import numpy as np
import pandas as pd
import datetime

df=pd.read_csv("static\\productsduplicate.csv")

unwanted=['is','and','','hello','i','my','a','an','the','of','mine','umm','ok','aa','would','like','to','email','address','id','we']

num=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen","couple","double","triple"]

date=["zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
        "nineth", "tenth", "eleventh", "twelveth", "thirteenth", "fourteenth", "fifteenth",
        "sixteenth", "seventeenth", "eighteenth", "nineteenth","twentieth","twenty","thirtieth","thirty"]

datey=["zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
        "nineth", "tenth", "eleventh", "twelveth", "thirteenth", "fourteenth", "fifteenth",
        "sixteenth", "seventeenth", "eighteenth", "nineteenth","twentieth","twenty","twenty-first",
        "twenty-second","twenty-third","twenty-fourth","twenty-fifth","twenty-sixth","twenty-seventh","twenty-eighth","twenty-ninth","thirtieth","thirty-first"]

month=['jan','feb','mar','apr','may','jun','jul','agu','sep','oct','nov','dec']
month3=['January','February','March','April','May','June','July','Agust','September','October','November','December']
Slot=["5:00 pm to 6:30 pm","6:30 pm to 8:00 pm","8:00 pm to 9:30pm","9:30 pm to 11:00pm"]

def showmenu():
    print("Here is our list of items\n\n",df.to_string(index=False),"\n")

def order():
    print("Sir please state your email address to proceed further.")
    statement=input()
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    global email
    email=''
    for x in objects:
        email+=x

    print("Thank You Sir, Now can  I get order please: ")
    statement=input()
    statement=statement.lower()
    statement=statement.split()
    dataf2=[x  for x in statement if x not in unwanted]
    global order
    order=[]
    quantity=[]  
    global quantity2
    quantity2=[]
    x=0 
    while x <len(dataf2):
        if dataf2[x] in df['Menu'].values:
            order.append(dataf2[x])
            if dataf2[x-1] in num:
                quantity.append(num.index(dataf2[x-1]))
            else:
                quantity.append(1)
        x+=1
    
    for x in quantity:
        if x==22:
            quantity2.append(3)
        elif x>19:
            quantity2.append(2)
        else:
            quantity2.append(x)
    dd=1

    while(dd):
        zz=0
        print("Thank You for your order here is the final list of your order:\n ")
        for x in range(len(order)):
            print(order[x]," : ",num[quantity2[x]])
        print("To Confirm: state Done \n To Update: state Update")
        while(1):
            print("when on update")
            statement=input()
            statement=statement.lower()
            statement=statement.split()
            dataf2=[x  for x in statement if x not in unwanted]
            print(dataf2)
            y=0
            while y <len(dataf2):
                if dataf2[y] =='update':
                    zz=1
                    print("\nOptions available are: \nAdd :to add new or existing products \nRemove: to reduce or delete existing prducts \nCombined Add and remove statements are accepted")
                    statement=input()
                    statement=statement.lower()
                    statement=statement.split()
                    dataf3=[x  for x in statement if x not in unwanted]
                    print(dataf3)
                    x=0
                    while x <len(dataf3):
                        if dataf3[x] == "add":
                            if dataf3[x+1] in df['Menu'].values:
                                if dataf3[x+1] not in order:
                                    order.append(dataf3[x+1])
                                    quantity.append(1)
                                else:
                                    quantity2[order.index(dataf3[x+1])]+=1
                                x+=1
                            elif dataf3[x+1] in num and x+2<len(dataf3):
                                if dataf3[x+2] in df['Menu'].values:
                                    if dataf3[x+2] not in order:
                                        order.append(dataf3[x+2])
                                        quantity.append(num.index(dataf2[x+1]))
                                    else:
                                        quantity[order.index(dataf3[x+2])]+=num.index(dataf3[x+1])
                                    x+=2
                        if dataf3[x] == "remove":
                            if dataf3[x+1] in df['Menu'].values:
                                if dataf3[x+1] in order:
                                    ind=order.index(dataf3[x+1])
                                    order.pop(ind)
                                    quantity.pop(ind)
                                x+=1
                            elif dataf3[x+1] in num and x+2<len(dataf3):
                                if dataf3[x+2] in df['Menu'].values:
                                    if dataf3[x+2] in order:
                                        quantity[order.index(dataf3[x+2])]-=num.index(dataf2[x+1])                   
                                       
                                    x+=2

                        x+=1                 

                elif dataf2[y] =='done':
                    zz=1
                    dd=0
                    break
                y+=1
                if zz==1 :
                    break
                if  zz==0 and y==len(dataf2):
                    print("Statement does not contains a valid responce\nPlease retry")
                
                
            if zz==1:
                break
        quantity2=[]
        for x in quantity:
            if x==22:
                quantity2.append(3)
            elif x>19:
                quantity2.append(2)
            else:
                quantity2.append(x)
        if dd==0 :
            break
    




def reserve():
    print("Sir please state your email address to proceed further.")
    statement=input()
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    global email
    email=''
    for x in objects:
        email+=x
    print("Thank You Sir, Please state the number of members: ")
    while(1):
        pp=1
        statement=input()
        statement=statement.lower()
        statement=statement.split()
        dataf2=[x  for x in statement if x not in unwanted]
        global members
        x=0
        while x <len(dataf2):
            if dataf2[x] in num:
                members=num.index(dataf2[x])
                if members==22 :
                    members=3
                elif members > 19 :
                    members=2
                break
            x+=1
            if x==len(dataf2):
                print("Statement does not contains a valid number of members\nPlease retry")
                pp=0
        if pp==1:
            break
            
        
    print("Please state the date of your arrival: ")
    global month2
    global date2
    while(1):
        pp=1
        statement=input()
        statement=statement.lower()
        statement=statement.split()
        month2=0
        date2=0 
        dataf2=[x  for x in statement if x not in unwanted]
        while x <len(dataf2):
            if dataf2[x][:3] in month:
                month2=month.index(dataf2[x][:3])
            elif dataf2[x] in date:
                date2=date.index(dataf2[x])
                if date2 <21:
                    pass
                elif date2 == 21 :
                    date2+=date.index(dataf2[x+1])
                    x+=1
                elif date2 == 22:
                    date2=30
                else :
                    date2=30+date.index(dataf2[x+1])
            x+=1
            if date2!=0 and month2!=0:
                break
            if x==len(dataf2):
                print("Statement does not contains a valid date\nPlease retry")
                pp=0
        if pp==1:
            break
            
    
    print("\nPlease the timeslot to book: ")
    print("Slot 1:",Slot[0],"\nSlot 2:",Slot[1],"\nSlot 3:",Slot[2],"\nSlot 4:",Slot[3])
    slot=-1
    while slot ==-1:
        statement=input()
        statement=statement.lower()
        statement=statement.split()
        dataf2=[x  for x in statement if x not in unwanted]
        x=0
        while x <len(dataf2):
            if dataf2[x] in num:
                slot=num.index(dataf2[x])-1
                if slot>4:
                    slot=-1
                    break
            elif dataf2[x] in date:
                slot=date.index(dataf2[x])-1
                if slot>4:
                    slot=-1
                    break
            x+=1
        if slot==-1:
            print("Invalid slot \nPlease state a valid slot: ")
        else:
            break
    
    print("Your reservation for",members,"members on ",datey[date2],month3[month2],"For Slot",slot+1,Slot[slot],"is done\nThank You\n")
            


hello="Hi, I am Guru from Aurdo, Please state your name to continue"
print(hello)
name=input()
name=name.split(" ")

name=[x  for x in name if x not in unwanted]
name2=''
for x in name:
    name2 +=x[0].upper()+x[1:]+" "

hello2="Hello "+name2+" How can I help You: \nI can \n1) Show Menu \n2) Take your order \n3) Reserve a table \n4) Say quit to stop"  
print(hello2)
x=1
while(x):
    statement=input()
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    if "menu" in objects:
        showmenu()
    elif "order" in objects:
        order()
    elif  "quit" in objects:
        print("Nice talk to you. Mr",name2,"Enjoy your meal.\nHope to serve you soon :)")
        break
    elif "reserve" in objects or "book" in objects:
        reserve()
    else:
        print("Not sure I got what you said could you please reapeat")
    print("Can I help you with anything else: \n I can \n1) Show Menu \n2) Take your order \n3) Reserve a table \n4) Say quit to stop")
    
# print(email)
