from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article'),
]