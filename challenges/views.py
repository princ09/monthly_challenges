from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls.base import reverse
# Create your views here.

monthly_challenges_list = {
    'january':'This works',
    'feburary':'Walk for at least 20 minutes daily',
    'march': 'learn django',
}

# def january(request):
#     return HttpResponse("This works")

# def feburary(request):
#     return HttpResponse("Walk for at least 20 minutes daily")

# def march(request):
#     return HttpResponse("learn django")   

def index(request):
    months =  list(monthly_challenges_list.keys())
    response = "<ul>"
    for month in months:
        redirect_path = reverse("monthly_challenges", args=[month])
        link = f"<li><a href=\"{redirect_path}\">{month.capitalize()}</a></li>"
        response+=link
    response+= "</ul>"
    return HttpResponse(response)


doRedirect = True

def monthly_challenges(request,month):
    if monthly_challenges_list.get(month):
        monthly_challenge = monthly_challenges_list[month]
        response = f"<h1>{monthly_challenge}</h1>"
        return HttpResponse(response) 
    else:
        return HttpResponse("<h1>Do your own thing</h1>")       


def monthly_challenges_by_number(request,month):
    if doRedirect:
        months = list(monthly_challenges_list.keys())
        
        if month > len(months):
            return HttpResponseNotFound("Invalid Request, Do your own things")
        
        redirect_month = months[month]
        # response = f"<h1>{redirect_month}</h1>"
        redirect_path = reverse("monthly_challenges", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        if month < len(list(monthly_challenges_list.values())) and month>=0:
            return HttpResponse(list(monthly_challenges_list.values())[month])
        else:
            return HttpResponse("Do your own thing")       
