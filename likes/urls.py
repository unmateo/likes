from django.urls import path

from .views import (
    HomeView,
    ItemListView,
    TagListView,
    SearchView,
)

app_name = 'likes'
urlpatterns = [
    path('tags/', TagListView.as_view(), name="tags"),
    path('items/', ItemListView.as_view(), name="items"),
    path('search/<str:query>', SearchView.as_view(), name="search"),
    path('', HomeView.as_view(), name="home"),
]
