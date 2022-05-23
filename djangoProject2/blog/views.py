from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail
# Create your views here.

def post_list(request):
    obj = Post.objects.all()
    paginator= Paginator(obj,3) #3 posts per page
    page=request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If the page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page': page,'posts': posts})

# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                             status='published',
#                             publish__year= year,
#                             publish__month= month,
#                             publish__day= day
#                             )
#
#
#     return render(request,'blog/post/detail.html',{'post':post})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments=post.comments.filter(active=True)
    new_comment=None

    if request.method =="POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False) #don't save in database yet
            new_comment.post=post #assign the current post to the comment
            new_comment.save() #save comment in the database
    else:
        comment_form= CommentForm()

    context = {
        'post': post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form
    }

    return render(request, 'blog/post/detail.html', context)

def post_share(request, post_id):
    #retreive post by id
    post = get_object_or_404(Post, id=post_id)
    sent = False
    if request.method == "POST":
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #passed validations
            cd=form.cleaned_data
            #send email
            post_url= request.build_absolute_uri(post.get_absolute_url())
            subject= f"{cd['name']} recommends you read " f"{post.title}"
            message= f"Read {post.title} at {post_url}\n\n" f"cd['name']\'s comments: {cd['comments']}"
            send_mail(subject,message,'youssef12aly@gmail.com',[cd['to']])
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post':post, 'form':form})



# Class based views
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'