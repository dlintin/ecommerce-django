from django.apps import AppConfig


class PembeliConfig(AppConfig):
    name = 'pembeli'

    def ready(self):
        import users.signals