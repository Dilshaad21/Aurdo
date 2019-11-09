from django.shortcuts import render, HttpResponse
from products.forms import resForm,Bill_View
from products.models import Restaurant,Audio_Bill
import pandas as pd
import numpy as np
import speech_recognition as sr

# Create your views here.


class Product(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'name': self.x,
            'price': self.y,
        }


def index(request):
    return render(request, 'index.html', context={"form": "forms"})


def menu(request):
    prod = Restaurant.objects.order_by("name")
    return render(request, 'menu.html', context={"products": prod})


def add_product(request):
    Form_View = resForm()
    if(request.method == "POST"):
        Form_View = resForm(request.POST)
        if(Form_View.is_valid()):
            Form_View.save(commit=True)
            prod = Restaurant.objects.order_by("name")
            pr_list = []
            pr_list2 = []
            for x in prod:
                pr_list.append(Product(x.name, x.price))
                pr_list2.append(Product(x.name, x.price))
                s1 = x.name+"s"
                s2 = x.name+"es"
                s3 = x.name[:-1]+"ies"
                pr_list2.append(Product(s1, x.price))
                pr_list2.append(Product(s2, x.price))
                pr_list2.append(Product(s3, x.price))
            df = pd.DataFrame.from_records([s.to_dict() for s in pr_list])
            df2 = pd.DataFrame.from_records([s.to_dict() for s in pr_list2])
            df.to_csv("static/products.csv")
            df2.to_csv("static/productsduplicate.csv")
            print("Form submitted")
            return render(request, 'forms.html', context={"form": Form_View, "addmore": "Product added successfully", "show": True})
        else:
            print("Form not valid")
    else:
        return render(request, "forms.html", context={"form": Form_View, "show": False})


not_name=['mobile','order','number','telephone','email','address']
num=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen","couple","double","triple"]

def Billing(p):
    df=pd.read_csv("static/productsduplicate.csv")
    data=p
    data=data.lower()
    data2=data.split()
    unwanted=['is','and','','hello','i','my','a','an','the','of','mine','umm','ok','aa','would','like','to','address','id','we']
    dataf2=[x  for x in data2 if x not in unwanted]
    name=[]
    email=[]
    order=[]
    quantity=[]
    cost_each=[]
    for x in range(len(dataf2)):
        if dataf2[x] == 'name' or dataf2 =='myself':
            x+=1
            name.append(dataf2[x])
            x+=1
            if dataf2[x] not in not_name:
                name.append(dataf2[x])
                x+=1
        elif dataf2[x] == 'email' or dataf2[x]== 'mail':
            x+=1
            if dataf2[x] == 'address' :
                x+=1
            while dataf2[x-1][-3:]!='com':
                email.append(dataf2[x])
                x+=1
        elif dataf2[x]=='order':
            x+=1
            while x<len(dataf2):
                if dataf2[x] in df['name'].values:
                    order.append(dataf2[x])
                    cost_each.append(df['price'].values[list(df['name'].values).index(dataf2[x])])
                    if dataf2[x-1] in num:
                        quantity.append(num.index(dataf2[x-1]))
                    else:
                        quantity.append(1)
                x+=1
    quantity2=[]
    for x in quantity:
        if x==22:
            quantity2.append(3)
        elif x>19:
            quantity2.append(2)
        else:
            quantity2.append(x)

    name2=''
    for x in name:
        name2 +=x[0].upper()+x[1:]+" "
    email2=''
    for x in email:
        email2 +=x
    total_price=[]
    for x in range(len(order)):
        total_price.append(quantity2[x]*cost_each[x])

    bill={"Order":order,"Quantity":quantity2,"Price each":cost_each,"Total price":total_price}
    bill=pd.DataFrame(bill)    
    return bill,email2,name2


def purchase(request):
    Audio_view=Bill_View()
    return render(request, 'purchase.html',context={"form":Bill_View})

def yourbill(request):
    Form_name=Bill_View()
    if(request.method=="POST"):
        Form_name=Bill_View(request.POST,request.FILES)
        if(Form_name.is_valid()):
            Form_name.save()
            AUDIO_FILE='media/audio/Audio1.wav'
            r=sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio= r.record(source)
            
            p=r.recognize_google(audio)
            items,email,name=Billing(p)
            return render(request,'bill.html',context={"bill":name})    