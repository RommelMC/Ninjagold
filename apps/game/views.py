from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
import random
import datetime
# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'game/index.html')

def money(request, place):
    time = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
    if request.method=='POST':
        if place=='farm':
            add = random.randrange(10,21)
            request.session['gold'] += add
            newstr="Earned " + str(add) + " golds from the farm! (" + time + ")\n"
            current = request.session['activities']
            current.append((newstr, 1))
            request.session['activities'] = current
        elif place=='cave':
            add = random.randrange(5,11)
            request.session['gold'] += add
            newstr="Earned " + str(add) + " golds from the cave! (" + time + ")\n"
            current = request.session['activities']
            current.append((newstr, 1))
            request.session['activities'] = current
        elif place=='house':
            add = random.randrange(5,11)
            request.session['gold'] += add
            newstr="Earned " + str(add) + " golds from the house! (" + time + ")\n"
            current = request.session['activities']
            current.append((newstr, 1))
            request.session['activities'] = current
        elif place=='casino':
            if random.randrange(0,2) == 0:
                add = random.randrange(0,51)
                request.session['gold'] += add
                new="Entered a casino and won " + str(add) + " golds! (" + time + ")\n"
                current = request.session['activities']
                current.append((new, 1))
                request.session['activities'] = current
            else:
                sub=random.randrange(0,51)
                request.session['gold'] -= sub
                new="Entered a casino and lost " + str(sub) + " golds! (" + time + ")\n"
                current = request.session['activities']
                current.append((new, 0))
                request.session['activities'] = current

        information={'gold': request.session['gold'], 'activities':request.session['activities']}
        return JsonResponse(information)

def clear(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    information={'gold': request.session['gold'], 'activities':request.session['activities']}
    return JsonResponse(information)

def token(request):
    token = get_token(request)
    return JsonResponse({'token':token, 'gold': request.session['gold'], 'activities':request.session['activities']})