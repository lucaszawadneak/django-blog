from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':"Lucas",
        'title': "Blog post 1",
        'content': 'Did you ever hear the tragedy of Darth Plagueis The Wise? ... Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying.',
        'date': 'Dec 16, 2021'
    },
        {
        'author':"Lucas 2",
        'title': "Blog post 2",
        'content': 'Second blog post',
        'date': 'Dec 16, 2021'
    }
]

def home(req):
    context = {
        'posts': posts
    }

    return render(req,'blog/home.html',context)
    
def about(req):
    context = {
        'title': "About"
    }
    
    return render(req,'blog/about.html',context)