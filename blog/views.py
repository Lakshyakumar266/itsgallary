from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib import messages
from .templatetags import extras
# Create your views here.


def BlogComment(request):
    if request.method == "POST":
        comment = request.POST.get('message')
        FName = request.POST.get('first_name')
        LName = request.POST.get('last_name')
        email = request.POST.get('email')
        postSno = request.POST.get('postSno')

        parentSno = request.POST.get('parentSno')

        post = Post.objects.get(sno=postSno)

        # first_name last_name email post parent content timeStamp

        if parentSno == None:
            comment = Comment(first_name=FName, last_name=LName,
                              email=email, content=comment, post=post)
            comment.save()
            messages.success(request, "Your Comment has been Posted succesfully.")
        else:
            parent = Comment.objects.get(sno=parentSno)
            comment = Comment(first_name=FName, last_name=LName,
                              email=email, content=comment, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your Reply has been Posted succesfully.")
            
    return redirect(f'/blog/blogpost/{post.slug}')


def BlogHome(request):
    blogs = Post.objects.all()
    context = {"posts": blogs}
    return render(request, 'blog/blog.html', context)


def BlogPost(request, slug):
    blog = Post.objects.filter(slug=slug).first()

    comments = Comment.objects.filter(post=blog, parent=None)
    replies = Comment.objects.filter(post=blog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {"post": blog, "comments":comments, "replyDict":replyDict}
    return render(request, 'blog/blogpost.html', context)
