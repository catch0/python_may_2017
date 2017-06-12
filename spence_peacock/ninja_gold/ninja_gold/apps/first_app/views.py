from django.shortcuts import render,redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
    gold_count=0;
    if 'gold_count' not in request.session:
        request.session['gold_count']=0
    if 'activity_log' not in request.session:
        request.session['activity_log']=[]
    return render(request, 'first_app/index.html')
def money(request):
    if request.POST['action']=='farm':
        farm_add = random.randrange(10,21)
        request.session['gold_count'] += farm_add
        string = "you earned" +str(farm_add) + "golds from the farm." + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    if request.POST['action']=='cave':
        cave_add = random.randrange(5,10)
        request.session['gold_count'] += cave_add
        string = "you earned" +str(cave_add) + "golds from the cave." + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    if request.POST['action']=='house':
        house_add = random.randrange(2,5)
        request.session['gold_count'] += house_add
        string = "you earned" +str(house_add) + "golds from the house." + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)   
    if request.POST['action']=='casino':
        casino_add = random.randrange(2,5)
        request.session['gold_count'] += casino_add
        string = "you earned" +str(casino_add) + "golds from the house." + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)   
    return redirect('/')
def clear(request):
        request.session['gold_count']=0
        return redirect('/')