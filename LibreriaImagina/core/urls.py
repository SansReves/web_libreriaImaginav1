from django.urls import path
from .views import * 

urlpatterns = [
    
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('catalogo/', catalogo, name="catalogo"),
    path('servicios/', servicios, name="servicios"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('registrouser/', registrouser, name="registrouser"),
    path('cerrarsesion/', cerrarsesion, name="cerrarsesion"),
    
    path('', home, name="home"),
    

]