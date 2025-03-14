from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # we need to let the app know about the new signals.py file:
    def ready(self):
        import users.signals
