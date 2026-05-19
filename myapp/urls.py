from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Home pages
    path('', views.result, name='result'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Student CRUD
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/',views.delete, name='delete'),

    # Other pages
    path('tablepage/', views.tablepage, name='tablepage'),
    path('index/', views.index, name='index'),
    path('testing/', views.testing, name='testing'),
    path('table/', views.table, name='table'),
    path('movies/', views.movies, name='movies'),
    path('services/', views.services, name='services'),
    path('reviews/', views.reviews, name='reviews'),
    path('sports/', views.sports, name='sports'),
    path('cart/', views.cart, name='cart'),
    path('fashion/', views.fashion, name='fashion'),
    path('shop/', views.shop, name='shop'),
    path('fashioncontact/', views.fashioncontact, name='fashioncontact'),
    path('mediaquery/', views.mediaquery, name='mediaquery'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)