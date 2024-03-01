from django.shortcuts import render

from .models import Post, PostSettings

# Create your views here.
def index(request):
    context = {
        "post_list": Post.objects.all()
    }
    # print(f"{Post.objects.order_by('text', '-title').all()}")
    if request.method == "POST":
        form_data = request.POST
        post_settings, _ = PostSettings.objects.get_or_create(pk=1)
        title=form_data['title']
        text=form_data['text']
        if len(text) > post_settings.text_len or len(title) > post_settings.title_len:
            context['msg'] = "Bad data"
        else: 
            post, _ = Post.objects.get_or_create(text=text, title=title)
            context['msg'] = "Success"
            print(f'{post=}')
        # post = Post()
        # post.title = form_data['title']
        # post.text = form_data['text']
        # post.save()
    return render(request, 'index.html', context=context)