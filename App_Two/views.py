from django.shortcuts import render
from django.http import HttpResponse
from App_Two.forms import myform
from App_Two.templatetags.filers import cut
from .models import Topic,Webpage,AccessRecord,user


# Create your views here.
def first_app(request):
    my_dict={'text':'hello all how are you','number':'200'}
    text_value = my_dict['text']
    filtered_text = cut(text_value, 'h')
    print(f"Original text: {text_value}")
    print(f"Filtered text: {filtered_text}")
    return render(request,'base.html',my_dict)

def first(request):
    my_text={'insert':"Hello All Im from views....!!!"}
    return render(request,'index.html',context=my_text)
def second(request):
    items_list=Topic.objects.order_by('date1')
    date_dict= {'access_items':items_list} 
   # my_text2={'insert':"Hello All Im from views....!!!"}
    return render(request,'second.html',context=date_dict)

def users(request):
    users_list=user.objects.order_by('Last_name')
    user_dict={'access_users':users_list}
    return  render(request,'user.html',context=user_dict)

def register(request):

    form=myform()
     
    if request.method =="POST":
        form= myform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return first_app(request)
        else:
            print("Form Invalid")
     
     
    return render(request,'register.html',{'form':form})