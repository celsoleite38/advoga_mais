from django.urls import path
from pacientes.views import index, pacientes, CreateCategoryView
urlpatterns = [
    path('index/', index ,name="index"),
    path('pacientes/', pacientes ,name="pacientes"),
    path ('category/add', 
            CreateCategoryView.as_view(),
            name='create_category'
         )
]
    
   