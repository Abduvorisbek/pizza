from django.urls import path
from pages.views import home_view, reserve_form

app_name = 'pages'


urlpatterns = [
    path('reserve/', reserve_form, name='reserve'),
    path('', home_view, name='home'),
]