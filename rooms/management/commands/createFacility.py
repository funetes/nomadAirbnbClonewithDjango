from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "create facilities"

    # args를 추가하지 않으면 매개변수 없이 파일명으로 command 설정 가능
    # def add_arguments(self, parser):
    #     parser.add_argument("--exec", help="custom commands execute", type=int)

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Successfully created."))

