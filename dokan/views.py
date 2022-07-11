from django.http import HttpResponse
from django.shortcuts import render
import pymongo
# Create your views here.
def index(request):
    
    client = pymongo.MongoClient("mongodb+srv://hasan:mahmud01@cluster0.dx63w.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    print(db)
    mydb = client["mobile"]
    mycol1 = mydb["mobile_details"]
    a=mycol1.find()
    return render(request,'home.html',{'data':a})