from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room
from users.models import User as model_user
from reservations.models import Reservation
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = "create Reservation"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="create fake reservation", type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_guests = model_user.objects.all()
        all_rooms = Room.objects.all()
        seeder.add_entity(
            Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(all_guests),
                "room": lambda x: random.choice(all_rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 10)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Successfully created."))

