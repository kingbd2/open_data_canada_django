from django.urls import path
from . import views

app_name = 'inventory_explorer'
urlpatterns = [
    path('', views.inventory_explorer, name='inventory_explorer'),
    path('<int:inventory_id>/', views.item_detail, name='item_detail'),
    # ex: /polls/5/results/
    path('<int:inventory_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/submit', views.get_data, name='get_data')
    ]
