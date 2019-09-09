from django.urls import path
from .views import clientes_list
from .views import clientes_new
from .views import cliente_update
from .views import cliente_delete


urlpatterns = [
    path('list/', clientes_list, name="cliente_list"),
    path('new/', clientes_new, name="clientes_new"),
    path('update/<int:id>/', cliente_update, name="cliente_update"),
    path('delete/<int:id>/', cliente_delete, name="cliente_delete"),
]