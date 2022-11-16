from django.urls import path
from world import views


urlpatterns = [
    # path('input_json',views.input_json),
    path('main_view/',views.main_view),
]