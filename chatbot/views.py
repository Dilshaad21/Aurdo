from django.shortcuts import render
import wikipedia
import pandas as pd 
import numpy as np
df=pd.read_csv("static\\productsduplicate.csv")
df2=pd.read_csv("static\\products.csv")
unwanted=['is','and','','hello','i','my','a','an','the','of','mine','umm','ok','aa','would','like','to','email','address','id','we','am','name','myself']

numw=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
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
name2=''
funk=0
def home(request):
    return render(request,'home.html')
# Create your views here.
def start(txt):
    name=txt.lower()
    name=name.split(" ")

    name=[x  for x in name if x not in unwanted]
    global name2
    name2=''
    for x in name:
        name2 +=x[0].upper()+x[1:]+" "
    global funk
    funk=1
    hello2="Hello "+name2+" How can I help You: \nI can \n1) Show Menu \n2) Take your order \n3) Reserve a table \n4) Say quit to stop"  
    return hello2

def process(txt):
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    ret=""
    global funk
    if "menu" in objects:
        ret ="Here is our list of items\n\n"+df2.to_string(index=False)+"\n"
        funk=3
    elif "order" in objects:
        ret="Sir please state your email address to proceed further."
        funk=10
    elif  "quit" in objects:
        ret="Nice talk to you. Mr"+name2+"Enjoy your meal.\nHope to serve you soon :)"
        funk=0
    elif "reserve" in objects or "book" in objects:
        ret="Sir please state your email address to proceed further."
        funk=30
    else:
        ret ="Not sure I got what you said could you please reapeat\n"
        funk=3
    return ret
    # print("Can I help you with anything else: \n I can \n1) Show Menu \n2) Take your order \n3) Reserve a table \n4) Say quit to stop")
    
def reserve(txt):
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    global email
    email=''
    for x in objects:
        email+=x
    ret= "Thank You Sir, Please state the number of members: "
    global funk 
    funk =31
    return ret

def reserve2(txt):
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    dataf2=[x  for x in statement if x not in unwanted]
    global members
    global funk
    x=0
    while x <len(dataf2):
        if dataf2[x] in num:
            members=num.index(dataf2[x])
            if members==22 :
                members=3
            elif members > 19 :
                members=2
            break
        elif dataf2[x] in numw:
            members=numw.index(dataf2[x])
            break
            
        x+=1
        if x==len(dataf2):
            ret="Statement does not contains a valid number of members\nPlease retry"
            funk=31
            return ret
    ret="Please state the date of your arrival: "
    funk =32
    return ret

  
def reserve3(txt):  
    global month2
    global date2
    global funk
  
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    month2=0
    date2=0 
    dataf2=[x  for x in statement if x not in unwanted]
    x=0
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
        elif dataf2[x][:-2] in numw:
            date2=numw.index(dataf2[x][:-2])
        elif dataf2[x] in numw:
            date2=numw.index(dataf2[x])

           
        x+=1
        if date2!=0 and month2!=0:
            break
        if x==len(dataf2):
            ret="Statement does not contains a valid date\nPlease retry"
            funk=32
            return ret

    ret="\nPlease select the timeslot to book: \nSlot 1:"+Slot[0]+"\nSlot 2:"+Slot[1]+"\nSlot 3:"+Slot[2]+"\nSlot 4:"+Slot[3]
    funk =33
    return ret


def reserve4(txt):
    global funk
    global slot
    slot=-1  
    statement=txt
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
        elif dataf2[x] in numw:
            slot=numw.index(dataf2[x])-1
            if slot>4:
                slot=-1
                break
        elif dataf2[x][:-2] in numw:
            slot=numw.index(dataf2[x][:-2])-1
            if slot>4:
                slot=-1
                break

        
        x+=1
    if slot==-1:
        ret="Invalid slot \nPlease state a valid slot: "
        funk=33
        return ret
    ret="Your reservation for "+str(members)+" members on "+datey[date2]+" "+month3[month2]+" For Slot "+str(slot+1)+" "+Slot[slot]+" is done\nThank You\n"
    funk =3
    return ret

def order(txt):
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    objects=[x  for x in statement if x not in unwanted]
    global email
    email=''
    for x in objects:
        email+=x

    ret="Thank You Sir, Now can  I get order please: "
    global funk
    funk =11
    return ret

def order2(txt):
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    dataf2=[x  for x in statement if x not in unwanted]
    global order
    order=[]
    global quantity
    quantity=[]  
    global quantity2
    quantity2=[]
    x=0 
    while x <len(dataf2):
        if dataf2[x] in df['name'].values:
            order.append(dataf2[x])
            if dataf2[x-1] in num:
                quantity.append(num.index(dataf2[x-1]))
            elif dataf2[x-1] in numw:
                quantity.append(numw.index(dataf2[x-1]))
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
    
    ret="Thank You for your order here is the final list of your order:\n "
    for x in range(len(order)):
        ret+=order[x]+" : "+num[quantity2[x]]+"\n"
    ret+="\nTo Confirm: state Done \n To Update: state Update"
    global funk
    funk=12
    return ret
    
def order3(txt):
    global funk
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    dataf2=[x  for x in statement if x not in unwanted]
    y=0
    while y <len(dataf2):
        if dataf2[y] =='update':
            ret="\nOptions available are: \nAdd :to add new or existing products \nRemove: to reduce or delete existing prducts \nCombined Add and remove statements are accepted"
            funk=20
            return ret

        elif dataf2[y] =='done':
            ret= "Thank You for shopping with us\n"
            funk = 3
            return ret
        y+=1
        if y==len(dataf2):
            ret="Statement does not contains a valid responce\nPlease retry\nTo Confirm: state Done \n To Update: state Update"
            funk=12
            return ret

            


def update(txt):            
    statement=txt
    statement=statement.lower()
    statement=statement.split()
    global order
    global quantity
    global quantity2
    global funk
    dataf3=[x  for x in statement if x not in unwanted]
    x=0
    while x <len(dataf3):
        if dataf3[x] == "add":
            if dataf3[x+1] in df['name'].values:
                if dataf3[x+1] not in order:
                    order.append(dataf3[x+1])
                    quantity.append(1)
                else:
                    quantity2[order.index(dataf3[x+1])]+=1
                x+=1
            elif dataf3[x+1] in num and x+2<len(dataf3):
                if dataf3[x+2] in df['name'].values:
                    if dataf3[x+2] not in order:
                        order.append(dataf3[x+2])
                        quantity.append(num.index(dataf2[x+1]))
                    else:
                        quantity[order.index(dataf3[x+2])]+=num.index(dataf3[x+1])
                    x+=2
            elif dataf3[x+1] in numw and x+2<len(dataf3):
                if dataf3[x+2] in df['name'].values:
                    if dataf3[x+2] not in order:
                        order.append(dataf3[x+2])
                        quantity.append(numw.index(dataf2[x+1]))
                    else:
                        quantity[order.index(dataf3[x+2])]+=numw.index(dataf3[x+1])
                    x+=2
        
        if dataf3[x] == "remove":
            if dataf3[x+1] in df['name'].values:
                if dataf3[x+1] in order:
                    ind=order.index(dataf3[x+1])
                    order.pop(ind)
                    quantity.pop(ind)
                x+=1
            elif dataf3[x+1] in num and x+2<len(dataf3):
                if dataf3[x+2] in df['name'].values:
                    if dataf3[x+2] in order:
                        quantity[order.index(dataf3[x+2])]-=num.index(dataf3[x+1])                   
                            
                        x+=2
            elif dataf3[x+1] in numw and x+2<len(dataf3):
                if dataf3[x+2] in df['name'].values:
                    if dataf3[x+2] in order:
                        quantity[order.index(dataf3[x+2])]-=numw.index(dataf3[x+1])    

                        x+=2  
        x+=1            
                            
    quantity2=[]
    for x in quantity:
        if x==22:
            quantity2.append(3)
        elif x>19:
            quantity2.append(2)
        else:
            quantity2.append(x)
    
    ret="Thank You for your order here is the final updated list of your order:\n "
    for x in range(len(order)):
        ret+=order[x]+" : "+num[quantity2[x]]+"\n"
    ret+="\nTo Confirm: state Done \n To Update: state Update"
    global funk
    funk=12
    return ret






def speech_to_text(request):
    data = request.POST.get('record')
    import speech_recognition as sr

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data =output
    global funk
    if funk==0:
        data2=start(data)
    elif funk==1:
        data2=process(data)
    elif funk==30:
        data2=reserve(data)
    elif funk==31:
        data2=reserve2(data)
    elif funk==32:
        data2=reserve3(data)
    elif funk==33:
        data2=reserve4(data)
    elif funk ==10:
        data2=order(data)
    elif funk ==11:
        data2=order2(data)
    elif funk ==12:
        data2=order3(data)
    elif funk == 20:
        data2=update(data)
    if funk==3:
        data2+="Can I help you with anything else: \n I can \n1) Show Menu \n2) Take your order \n3) Reserve a table \n4) Say quit to stop"
        funk=1
    elif funk==0:
        cost_each=[]
        for x in range(len(order)):
            cost_each.append(df['price'].values[list(df['name'].values).index(order[x])])
        total_price=[]
        for x in range(len(order)):
            total_price.append(quantity2[x]*cost_each[x])
        bill={"Order":order,"Quantity":quantity2,"Price_each":cost_each,"Total_price":total_price}
        items=pd.DataFrame(bill)    
        summ=items["Total_price"].sum()
        return render(request,'bill2.html',context={"Name":name2,"Email":email,'Items':items.to_dict('records'),"sum":summ}) 


    
    return render(request,"home.html",context={"data":data,"data2":data2})
