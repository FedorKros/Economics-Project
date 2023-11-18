"""
URL configuration for PeekOnEcon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
# These 2 conflict with each other
# from diagrams import views
# from quizzes import views


# from diagrams import views
# from quizzes import views as qviews


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('homepage.urls')),
    path('diagrams/', include('diagrams.urls')),
    path('quizzes/', include('quizzes.urls')),

    # path("", views.home, name = "home"),
    # # path('', include(('home.urls', 'home'), namespace='home')),
    # path("about/", views.about_us, name = "about_us"),
    # path("topics/", views.topics, name = "topics"),
    # path("all_list/", qviews.all_list, name = "quizzes"),

    # # Competitive markets
    # path("demand/", views.demand, name = "demand"),
    # path("supply/", views.supply, name = "supply"),
    # path("demandandsupply", views.demand_and_supply, name = "demand_and_supply"),
    # path("ppc/", views.ppc, name = "ppc"),
    # path("veblengoods/", views.veblen, name = "veblengoods"),
    # path("producerandconsumersurplus/", views.proandconsurplus, name = "producerandconsumersurplus"),
    
    # # Elasticity
    # path("yed/", views.yed, name = "yed"),
    # path("ped/", views.ped, name = "ped"),
    # path("pes/", views.pes, name = "pes"),
    
    # # The role of government in microeconomics
    # path("indirecttaxation/", views.indirecttaxation, name = "indirect_taxation"),
    # path("subsidy/", views.subsidy, name = "subsidy"),
    # path("maximum_price/", views.maximum_price, name = "maximum_price"),
    # path("minimum_price/", views.minimum_price, name = "minimum_price"),
    # path("minimum_wage/", views.minimum_wage, name = "minimum_wage"),

    # # Market failure
    # path("merit_goods/", views.merit_goods, name = "merit_goods"),
    # path("demerit_goods/", views.demerit_goods, name = "demerit_goods"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


