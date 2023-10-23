from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # apis
    path('display_search/<str:userinput>',views.display_search,name="display_search")
]