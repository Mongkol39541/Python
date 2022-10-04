from django.urls import path
from .views import index, blogDetail, searcCategory, searcWriter

urlpatterns = [
    path('', index),
    path('blog/<int:id>', blogDetail, name='blogDetail'),
    path('blog/category/<int:cat_id>', searcCategory, name="searcCategory"),
    path('blog/writer/<str:writer>', searcWriter, name="searcWriter")
]