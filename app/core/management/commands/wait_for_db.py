"""
Django command to wait for the database to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to wait for database to be available """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(database)