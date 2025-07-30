from django.urls import path
from url import views

urlpatterns = [
    path('', views.simple_ui, name='simple_ui'),  # root path handled here
    path('url/<str:hash>', views.redirect_original_url, name='redirect_original_url'),
    path('url', views.create_short_url, name='create_short_url'),
    path('url/details/<str:hash>', views.get_url_details, name='get_url_details'),
]