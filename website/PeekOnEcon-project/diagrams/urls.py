from django.urls import path
from . import views

urlpatterns = [
    
    path("about/", views.about_us, name = "about_us"),
    path("topics/", views.topics, name = "topics"),
    # path("all_list/", qviews.all_list, name = "quizzes"),

    # Competitive markets
    path("demand/", views.demand, name = "demand"),
    path("supply/", views.supply, name = "supply"),
    path("demandandsupply", views.demand_and_supply, name = "demand_and_supply"),
    path("ppc/", views.ppc, name = "ppc"),
    path("veblengoods/", views.veblen, name = "veblengoods"),
    path("producerandconsumersurplus/", views.proandconsurplus, name = "producerandconsumersurplus"),
    
    # Elasticity
    path("yed/", views.yed, name = "yed"),
    path("ped/", views.ped, name = "ped"),
    path("pes/", views.pes, name = "pes"),
    
    # The role of government in microeconomics
    path("indirecttaxation/", views.indirecttaxation, name = "indirect_taxation"),
    path("subsidy/", views.subsidy, name = "subsidy"),
    path("maximum_price/", views.maximum_price, name = "maximum_price"),
    path("minimum_price/", views.minimum_price, name = "minimum_price"),
    path("minimum_wage/", views.minimum_wage, name = "minimum_wage"),

    # Market failure
    path("merit_goods/", views.merit_goods, name = "merit_goods"),
    path("demerit_goods/", views.demerit_goods, name = "demerit_goods"),
    
]