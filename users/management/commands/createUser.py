from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "this is my first custom commands"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, help="create fake users", type=int)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Successfully created."))

