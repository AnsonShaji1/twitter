from django.shortcuts import render
from .models import Post
from .forms import PostForm

import requests
from requests_oauthlib import OAuth1
import json 




def enter_details(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            CONSUMER_KEY ="Cx5ZG3uXQqys37ja43INoFZlP"
            CONSUMER_SECRET ="CdQeJoAz8Lt1fSPCzmrm00fIi9npRe3Y58uE1V7CzmN6QeXTfe"


            OAUTH_TOKEN = "1142054935-s8h7AY5lRa8JOvHkCWi6QYG40Sz1b8osS5SQB8f"
            OAUTH_TOKEN_SECRET ="u9RxwU3va6ykZm98UZO6gl6q1migsdJ9biYFHpddg11nq"


            url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
            auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
            requests.get(url, auth=auth)
            print("valueeee="+ str(request.POST['name']))
            

            r=requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q="+ str(request.POST['name']) +"&count=10",auth=auth)
            br=r.json()
            
            a=br['statuses']
            
            post.save()
            
            return render(request,'twitter/content.html',{'a':a})
    else:
        form=PostForm()
        return render(request,'twitter/index.html',{'form':form})




            
        
