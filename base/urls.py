# Importar la función "path" y el módulo de vistas "views" desde Django
from django.urls import path
from .views import TaskList

# Crear una lista de patrones de URL
urlpatterns = [
    # Especificar la URL raíz del sitio web (con ""), que activará la vista "taskList"
     path('', TaskList.as_view(), name='tasks'),
]
