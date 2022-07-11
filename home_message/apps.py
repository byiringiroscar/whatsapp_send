from django.apps import AppConfig


class HomeMessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_message'
    def ready(self):
        import home_message.signals
