from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import Create
from .models import Posting
from django.core.paginator import Paginator
#
# def home(request):
#     posts = Posting.objects.all()
#     return render(request, 'blog/home.html', {'posts': posts}) #home.html 리턴

def intro(request):
    return render(request,'blog/intro.html')

# def evaluate(request, pk):
#     post = Posting.objects.get(pk=pk)
#     return render(request, 'blog/evaluate.html', {'post':post})
def evaluate(request, posting_id):
    post = get_object_or_404(Posting, pk=posting_id)
    return render(request, 'blog/evaluate.html', {'post': post})

def create(request):
    if request.method == 'POST':
        form = Create(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            return redirect('/home')
    else:
        form = Create()
        return render(request, 'blog/create.html', {'form': form})


def update(request, posting_id):
    notice = Posting.objects.get(id=posting_id)

    if request.method == "POST":
        form = Create(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('/home/' + str(posting_id))
    else:
        notice = Posting.objects.get(id=posting_id)
        form = Create(instance=notice)
        context = {
            'form': form,
            'edit': '수정하기',
         }
        return render(request, "blog/update.html", context)

def delete(request, posting_id):
    de = Posting.objects.get(id=posting_id)
    de.delete()
    return redirect('/home/')
# return redirect('/home/'+str(posting_id)+ '/delete')

def home(request):

    page = request.GET.get('page', '1')  # 페이지

    posts = Posting.objects.order_by('-pub_date')

    # 페이징처리
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {'posts': page_obj}
    return render(request, 'blog/home.html', context)