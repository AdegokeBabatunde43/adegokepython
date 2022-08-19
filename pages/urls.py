from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('remove/<int:id>', views.remove, name='remove'),
] 