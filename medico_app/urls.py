from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home),
    path('calc/',views.calc),
    path('calc/add',views.add)

    


]
