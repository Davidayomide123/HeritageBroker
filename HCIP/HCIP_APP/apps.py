from django.apps import AppConfig


class HcipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HCIP_APP'


    def ready(self):
        from . import signals  # Import signals to connect them