from django.apps import AppConfig


class RemindListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminder'
    verbose_name = 'Tasks to be reminded of'
