from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'Evaan', 'age' : 17,
         
         'fav_food':[
             'Burger','Pizza','Pasta'
         ],
         'b_day': datetime.datetime.now() , 
         
         
         
         }
    return render(request,'home.html',d)