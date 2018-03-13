from inventory_explorer.models import Inventory
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count = Inventory.objects.from_csv('inventory_clean_date.csv')
        print ("{} records inserted".format(insert_count))
