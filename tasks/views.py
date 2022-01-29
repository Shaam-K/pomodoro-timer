from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks.models import tasks_snippet
from tasks.forms import task_snippet_form
from datetime import datetime
from dateutil import tz
from django.core.paginator import Paginator
from django.shortcuts import redirect
# Create your views here.

def tasks(request):
    return render(request, "tasks.html")

def tasks_form(request):
    if request.method == 'POST':
        form = task_snippet_form(request.POST)

        print("form works")
        
        if form.is_valid():
            form.save()
            task = form.cleaned_data['task_details']
            date = form.cleaned_data['due_date']
            form_accepted = 'yes'

            values = {
                'task' : str(task),
                'date': str(date),
                'form_accepted': str(form_accepted)
            }


            final_data = []

            final_data.append(values)

            context = {'task_data': final_data}

            redirect('/view/')
            return render(request, 'tasks.html', context)

        form = task_snippet_form()

        return render(request,'tasks.html',{'form': form})


def task_database(request):
    task_database_batch = tasks_snippet.objects.all().order_by('-id')[:20]

    p = Paginator(task_database_batch,5)

    page = request.GET.get('page')

    batch_pages = p.get_page(page)

    context = {'task_db': task_database_batch, 'pages': batch_pages}
    return render(request, 'tasks.html', context)
    
    