from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room, RoomType, Photo, Amenity, Facility, HouseRule
from users.models import User as model_user
import random


class Command(BaseCommand):
    help = "create Rooms"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, help="create fake rooms", type=int)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = model_user.objects.all()
        all_types = RoomType.objects.all()
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        houseRule = HouseRule.objects.all()
        seeder.add_entity(
            Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_types),
                "guests": lambda x: random.randint(0, 20),
                "price": lambda x: random.randint(0, 1000),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 8),
                "baths": lambda x: random.randint(1, 5),
                "name": lambda x: seeder.faker.address(),
            },
        )

        created_rooms = seeder.execute()
        pk_list = list(created_rooms.values())[0]
        for pk in pk_list:
            room = Room.objects.get(pk=pk)

            for i in range(random.randint(3, 8)):
                Photo.objects.create(
                    caption=seeder.faker.text(),
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                    room=room,
                )
            for a in amenities:
                magic_number = random.randint(0, 30)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 30)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in houseRule:
                magic_number = random.randint(0, 30)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS("Successfully created."))

