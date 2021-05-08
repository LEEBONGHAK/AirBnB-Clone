import random
from random import choice, seed
from django.core.management.base import BaseCommand
from django.db.models.query_utils import select_related_descend
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many times do you want to create rooms?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # 유저를 데이터베이스에서 가져오기 (데이터베이스가 크다면 .all()은 권장되지 않음)
        all_users = users_models.User.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                # host에 무작위 user을 지정해 주는 익명의 함수를 제작
                "host": lambda x: random.choice(all_users),
                # room type에 무작위 room type을 지정해 주는 익명의 함수를 제작
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))