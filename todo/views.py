# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . models import TodoList
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from django.views import generic

# class Todo_main(generic.TemplateView):
#     def get(self, request, *args, **kwargs):
#         template_name = 'todo_main/index.html'
#         todo_list = TodoList.objects.all()
#         return render(request, template_name, {'todo_list':todo_list})
def index(request):
    todo_list = TodoList.objects.all()
    return render(request, 'todo/index.html', {'todo_list':todo_list})


def detail(request, todolist_id):
    de_post = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todo/detail.html', {'de_post': de_post})

# @login_required
def insert(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/todo/')

        else:
            return redirect('/todo/')
    else:
        form = TodoForm()
        return render(request, 'todo/insert.html',{'form':form})

def edit(request, todolist_id):
    notice = TodoList.objects.get(id=todolist_id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            # messages.success(request, "수정되었습니다.")
            return redirect('/todo/' + str(todolist_id))
    else:
        notice = TodoList.objects.get(id=todolist_id)
        form = TodoForm(instance=notice)
        context = {
            'form': form,
            'edit': '수정하기',
         }
        return render(request, "todo/edit.html", context)

def remove(request, todolist_id):
    de = TodoList.objects.get(id=todolist_id)
    de.delete()
    return redirect('/todo/')
#
# def detail(request, TodoList_no):
#     detail_todo = get_object_or_404(TodoList, pk=TodoList_no)
#     return render(request, 'todo_main/detail.html', {'detail_todo':detail_todo})
