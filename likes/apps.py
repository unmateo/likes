from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class LikesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'likes'

class LikesAdminConfig(AdminConfig):
    default_site = 'likes.admin.LikesAdminSite'
