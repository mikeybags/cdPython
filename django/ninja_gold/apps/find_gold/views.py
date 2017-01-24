from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, 'find_gold/index.html')

def process_money(request, choice):
    timestamp = str(datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    if choice == "farm":
        earnings = random.randrange(10,21)
        request.session['gold'] += earnings
        activity_log = "You have earned " + str(earnings) + " gold from the farm! " + timestamp
        request.session['activity_log'].append(activity_log)
    if choice == "cave":
        earnings = random.randrange(5,11)
        request.session['gold'] += earnings
        activity_log = "You have earned " + str(earnings) + " gold from the cave! " + timestamp
        request.session['activity_log'].append(activity_log)
    if choice == "house":
        earnings = random.randrange(2,6)
        request.session['gold'] += earnings
        activity_log = "You have earned " + str(earnings) + " gold from the house! " + timestamp
        request.session['activity_log'].append(activity_log)
    if choice == "casino":
        if request.session['gold'] < 10:
            request.session['gold'] += 0 #my computer is dumb and it won't work without this line for some reason.
            activity_log = "You must have at least 10 gold to gamble! Come back when you have more! " + timestamp
            request.session['activity_log'].append(activity_log)
        else:
            result = random.randrange(-50,51)
            if result == 0:
                request.session['gold'] += 0 #my computer is dumb and it won't work without this line for some reason.
                activity_log = "You came out even!"
                request.session['activity_log'].append(activity_log)
            elif result < 0:
                if (request.session['gold'] - result) <= 0:
                    activity_log = "You have lost all " + str(request.session['gold']) + " gold at the casino! " + timestamp
                    request.session['gold'] = 0
                    request.session['activity_log'].append(activity_log)
                else:
                    request.session['gold'] += result
                    result *= -1
                    activity_log = "You lost " + str(result) + " gold at the casino. Better luck next time! " + timestamp
                    request.session['activity_log'].append(activity_log)
            else:
                activity_log = "You have won " + str(result) + " gold at the casino. Try for more? " + timestamp
                request.session['gold'] += result
                request.session['activity_log'].append(activity_log)

    return redirect('/')
