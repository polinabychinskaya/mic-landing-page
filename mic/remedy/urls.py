from django.urls import path
from . import views
app_name = 'remedy'

urlpatterns = [
    path('magvit/', views.Magvit.as_view(), name='magvit'),
    path('validol/', views.Validol.as_view(), name='validol')
]