import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from threading import Thread

class Command(BaseCommand):
    help = 'Starts the Gunicorn server and adds the django-crontab jobs'

    def handle(self, *args, **kwargs):

        # Add the django-crontab jobs
        call_command('crontab', 'add')
        call_command('crontab', 'show')

        # Start the Gunicorn server in a new thread
        #Thread(target=os.system, args=('python manage.py runserver',)).start()
        Thread(target=os.system, args=('gunicorn smartlearning.wsgi',)).start()
