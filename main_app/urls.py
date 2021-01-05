from django.urls import path, include
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('get_quote/', views.get_quote, name='get_quote'),
    # path('<int:year>/', views.diary),
    # path('<int:year>/<str:name>/', views.diary),
]