from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room
from users.models import User as model_user
from lists.models import List
import random


class Command(BaseCommand):
    help = "create List"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, help="create fake rooms", type=int)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = model_user.objects.all()
        all_rooms = Room.objects.all()
        seeder.add_entity(List, number, {"user": lambda x: random.choice(all_users)})
        created = seeder.execute()
        clean = list(created.values())[0]
        for pk in clean:
            list_model = List.objects.get(pk=pk)
            randRooms = all_rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*randRooms)
        self.stdout.write(self.style.SUCCESS("Successfully created."))

