from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('contact/', views.contact, name='contact'),
    path('api/search/', views.search_api, name='search_api'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots'),
]
