from django.urls import path
from .views import Home, ArtDetail, AddPost, EditPost, DeletePost, About, pageNotFound, AddCategoryView, CategoryView, CategoryListView
from django.conf.urls import handler404

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArtDetail.as_view(), name='artdetail'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('article/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('about/', About.as_view(), name='about'),
    path('addcategory/', AddCategoryView.as_view(), name='addcategory'),
    path('category/<str:cats>', CategoryListView, name='category_list'),
    path('category-list/', CategoryView, name='category'),
]

