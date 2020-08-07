from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'check_out'

    def ready(self):
        import check_out.signals
