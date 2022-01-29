from typing import final
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
import math
from tasks.models import tasks_snippet
from tasks.forms import task_snippet_form
# Create your views here.
def timer(request):
    return render(request, "timer.html")

def timer_form(request):
    if request.method == 'POST':
        hours = request.POST['hour']
        minutes = request.POST['min']
        break_response = request.POST['break']

        zero = "no"
        hours_int = int(hours)
        minutes_int = int(minutes)
        break_response_str = str(break_response)

        hours_sec = hours_int * 60 * 60
        minutes_sec = minutes_int * 60
        total_sec = hours_sec + minutes_sec 

        if hours_sec == 0 and minutes_sec == 0:
            zero = "yes"

        if break_response_str == 'Yes':
            break_amount = math.floor(total_sec // 1500)
            break_time = break_amount * 5
            break_time_seconds = break_time * 60
        else:
            break_amount = 0
            break_time = 0
            break_time_seconds = 0
        
        total_time = total_sec + break_time_seconds
        
        values = {
            'seconds': int(total_sec),
            'break_amount': int(break_amount),
            'break_time': int(break_time_seconds),
            'total_time': int(total_time),
            "zero": str(zero),
            "break_response": break_response_str
        }
        
        timer_data = []

        timer_data.append(values)

        context = {'timer_data' : timer_data}

    return render(request, "timer.html", context)


def timer_task_detail(request):
    task_database_batch = tasks_snippet.objects.all().order_by('-id')[:5]

    context = {'timer_db': task_database_batch}

    return render(request, 'timer.html', context)
