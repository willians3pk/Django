from django.urls import path
from . import views

# nome do app, para direcionar as urls!
app_name = "produtos"

urlpatterns = [
    # execulta o metodo post_list na views.py, se não for passado nenhum argumento na url
    # do navegador.
    path("", views.post_list, name="list"),
    # passa o id como parametro na url
    path("<int:id>/", views.post_detalhes),
    path("about.html/", views.post_about),
    path("services.html/", views.post_services),

]