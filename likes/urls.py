from django.urls import path

from .views import HomeView, ItemListView, TagListView

app_name = 'likes'
urlpatterns = [
    path('tags/', TagListView.as_view(), name="tags"),
    path('items/', ItemListView.as_view(), name="items"),
    path('', HomeView.as_view(), name="home"),
]
