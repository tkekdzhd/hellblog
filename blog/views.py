from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-id')  #Blog 객체를 다 가져오겠다
    return render(request,'blog/home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog_detail})

# C - new
def new(request):
    return render(request, 'blog/new.html') # 요청이 들어오면 render라는 함수를 통해서 new.html파일을 띄워줘라.


# C - create
def create(request):
    blog = Blog() #붕어빵 틀
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/' + str(blog.id))

# D - edit
def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/edit.html',{'blog':blog}) 


# U - update 실제 글이 수정되는 동작
def update(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    # 붕어빵 틀을 다 채웠다.
    blog.save()

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

# D - delete
def delete(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('home')