from django.apps import AppConfig


class HistoricalDataConfig(AppConfig):
    name = 'historical_data'

    def ready(self):
        import historical_data.signals
