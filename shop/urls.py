from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prodt_cat'),
    path('<slug:c_slug>/<slug:p_slug>',views.detail,name='detail'),
    path('search',views.search,name='search'),
]