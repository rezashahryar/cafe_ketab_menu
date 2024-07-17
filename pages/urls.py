from django.urls import path
from . import views

# create your urls here

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('category/<slug:slug>/products/', views.CategoryObjects.as_view(), name='category_objects'),
]

