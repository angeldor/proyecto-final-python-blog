from django.urls import path
from .views import Home, ArtDetail, AddPost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArtDetail.as_view(), name='artdetail'),
    path('addpost/', AddPost.as_view(), name='addpost')
    
]
