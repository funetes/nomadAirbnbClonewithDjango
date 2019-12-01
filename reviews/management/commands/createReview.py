from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room
from users.models import User as model_user
from reviews.models import Review
import random


class Command(BaseCommand):
    help = "create Review"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, help="create fake rooms", type=int)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = model_user.objects.all()
        all_rooms = Room.objects.all()
        seeder.add_entity(
            Review,
            number,
            {
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Successfully created."))

