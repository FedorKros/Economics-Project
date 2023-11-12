from django.shortcuts import render


# Paths
micro = 'diagrams/themes/micro/'
macro = 'diagrams/themes/macro/'
world = 'diagrams/themes/global/'  


# Main
def topics(request):
    return render(request, 'diagrams/topics.html')

def about_us(request):
    return render(request, 'diagrams/about.html')


# Microeconomics
def demand(request):
    return render(request, micro + 'demand.html')

def demand_and_supply(request):
    return render(request, micro + 'demand_and_supply.html')

def supply(request):
    return render(request, micro + 'supply.html')

def ppc(request):
    return render(request, micro + 'ppc.html')

def veblen(request):
    return render(request, micro + 'veblengoods.html')

def proandconsurplus(request):
    return render(request, micro + 'producer_and_consumer_surplus.html')
    
def yed(request):
    return render(request, micro + 'yed.html')

def ped(request):
    return render(request, micro + 'ped.html')

def pes(request):
    return render(request, micro + 'pes.html')

def indirecttaxation(request):
    return render(request, micro + 'indirect_taxation.html')

def subsidy(request):
    return render(request, micro + 'subsidy.html')

def maximum_price(request):
    return render(request, micro + 'maximum_price.html')

def minimum_price(request):
    return render(request, micro + 'minimum_price.html')

def minimum_wage(request):
    return render(request, micro + 'minimum_wage.html')

def merit_goods(request):
    return render(request, micro + 'merit_goods.html')

def demerit_goods(request):
    return render(request, micro + 'demerit_goods.html')





# Macroeconomics

def business_cycle(request):
    return render(request, macro + 'business_cycle.html')
    
def new_classical(request):
    return render(request, macro + 'new_classical.html')
    
def keynesian(request):
    return render(request, macro + 'keynesian.html')

def inflation(request):
    return render(request, macro + 'inflation.html')


# Global economics

def free_trade(request):
    return render(request, world + 'free_trade.html')

def tariffs(request):
    return render(request, world + 'tariffs.html')

def quotas(request):
    return render(request, world + 'quotas.html')

def subsidies_tp(request):
    return render(request, world + 'subsidies_tp.html')

