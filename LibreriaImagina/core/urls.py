from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name="home"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('catalogo/', catalogo, name="catalogo"),
    path('servicios/', servicios, name="servicios"),
    path('quienessomos/', quienessomos, name="quienessomos"),

    

]