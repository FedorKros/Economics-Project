from django.shortcuts import render

# def home(request):
#     return render(request, 'diagrams/home.html')

def topics(request):
    return render(request, 'diagrams/topics.html')

def about_us(request):
    return render(request, 'diagrams/about.html')

def demand(request):
    return render(request, 'diagrams/themes/demand.html')

def demand_and_supply(request):
    return render(request, 'diagrams/themes/demand_and_supply.html')

def supply(request):
    return render(request, 'diagrams/themes/supply.html')

def ppc(request):
    return render(request, 'diagrams/themes/ppc.html')

def veblen(request):
    return render(request, 'diagrams/themes/veblengoods.html')

def proandconsurplus(request):
    return render(request, 'diagrams/themes/producer_and_consumer_surplus.html')
    
def yed(request):
    return render(request, 'diagrams/themes/yed.html')

def ped(request):
    return render(request, 'diagrams/themes/ped.html')

def pes(request):
    return render(request, 'diagrams/themes/pes.html')

def indirecttaxation(request):
    return render(request, 'diagrams/themes/indirect_taxation.html')

def subsidy(request):
    return render(request, 'diagrams/themes/subsidy.html')

def maximum_price(request):
    return render(request, 'diagrams/themes/maximum_price.html')

def minimum_price(request):
    return render(request, 'diagrams/themes/minimum_price.html')

def minimum_wage(request):
    return render(request, 'diagrams/themes/minimum_wage.html')

def merit_goods(request):
    return render(request, 'diagrams/themes/merit_goods.html')

def demerit_goods(request):
    return render(request, 'diagrams/themes/demerit_goods.html')