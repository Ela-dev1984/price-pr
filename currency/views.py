from django.shortcuts import render,HttpResponse

from  gheymat.currency import USD,EUR,GBP
def home(request):
     return HttpResponse("welcome")
def usd(request):
    USD_price=USD(toman=True,beauty=False)
    return HttpResponse(F"gheymate usd emrooz:{USD_price}.") 
def eur(request):
    EUR_price=EUR(toman=True,beauty=False)
    return HttpResponse(F"gheymate eur emrooz:{EUR_price}.") 
def gbp(request):
    GBP_price=GBP(toman=True,beauty=False)
    return HttpResponse(F"gheymate usd emrooz:{GBP_price}.") 

