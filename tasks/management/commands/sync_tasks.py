from django.core.management.base import BaseCommand
import requests
from tasks.models import PendingTask

class Command(BaseCommand):
    help = 'Sincroniza los pendientes desde el API de Parra’s Dev'

    def handle(self, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/todos'
        response = requests.get(url)
        if response.status_code == 200:
            todos = response.json()
            for todo in todos:
                PendingTask.objects.update_or_create(
                    api_id=todo['id'],
                    defaults={
                        'user_id': todo['userId'],
                        'title': todo['title'],
                        'completed': todo['completed']
                    }
                )
            self.stdout.write(self.style.SUCCESS('Tareas sincronizadas exitosamente'))
        else:
            self.stdout.write(self.style.ERROR('Error al conectar con el API'))