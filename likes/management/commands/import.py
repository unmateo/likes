from django.core.management.base import BaseCommand, CommandError
from likes.models import Tag, Item


class Command(BaseCommand):
    help = 'Import items from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']
        print(filename)
        parsed_users = 0
        parsed_tags = 0
        created_users = 0
        created_tags = 0
        try:
            with open(filename) as file:
                current_tags = []
                base_url = "https://instagram.com/{username}"
                for line in file:
                    try:
                        if not line:
                            continue
                        elif line[0] == "#":
                            tag_names = line.strip().split("#")[1:]
                            current_tags = []
                            for tag_name in tag_names:
                                tag, created = Tag.objects.get_or_create(name=tag_name.upper())
                                current_tags.append(tag.id)
                                parsed_tags += 1
                                created_tags += created
                        else:
                            username = line.strip()
                            link = base_url.format(username=username)
                            item, created = Item.objects.get_or_create(
                                name=username,
                                defaults={"link": link}
                            )
                            item.tags.clear()
                            item.tags.add(*current_tags)
                            parsed_users += 1
                            created_users += created
                    except Exception as e:
                        print(e)
                        continue
            parsed = f"Parsed {parsed_users} users and {parsed_tags} tags."
            created = f"Created {created_users} users and {created_tags} tags."
            self.stdout.write(self.style.SUCCESS(parsed))
            self.stdout.write(self.style.SUCCESS(created))
        except Exception as e:
                raise CommandError(str(e))
