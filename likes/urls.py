from django.urls import path

from .views import ItemListView, TagListView

app_name = 'likes'
urlpatterns = [
    path('tags/', TagListView.as_view()),
    path('items/', ItemListView.as_view()),
]
