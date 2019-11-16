from django.apps import AppConfig

# importamos signals para que queden listas
# y esten en el arranque de la app

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals