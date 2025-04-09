from django.urls import path
from . import views

urlpatterns = [
    # path('pagina/', page_views.page, name="page")
    path('pagina/<str:slug>', views.page, name="page")
]
