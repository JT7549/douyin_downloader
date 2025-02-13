from django.core.management.base import BaseCommand
from downloader.models import UserInfo

class Command(BaseCommand):
    help = 'Insert data into UserInfo model'

    def handle(self, *args, **options):
        data_list = [
            { 'name': 'John', 'age': 25},
            { 'name': 'Alice', 'age': 30}
        ]
        for data in data_list:
            UserInfo.objects.create(
                #id=data['id'],
                name=data['name'],
                age=data['age']
            )
        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))