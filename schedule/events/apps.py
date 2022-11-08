from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule.events'

    def ready(self):
        try:
            import schedule.events.signals  # noqa F401
        except ImportError:
            pass