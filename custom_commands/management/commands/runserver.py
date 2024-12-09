import os
import subprocess
import threading

from django.contrib.staticfiles.management.commands.runserver import (
    Command as StatisFilesRunserverCommand
)
from django.utils.autoreload import DJANGO_AUTORELOAD_ENV


class Command(StatisFilesRunserverCommand):
    """
    Runs Django and pnpm server.
    """

    help = (
        "Starts a lightweight web server for development and also serve staticfiles",
        "And runs pnpm tailwind worker in another thread"
    )

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--tw-command",
            dest="tw_command",
            default="pnpm tw",
            help="This command will be run in another thread (If using npm or yarn then provide a command.)"
        )

    def run(self, **options):
        """
        Run the server with tailwind in the background.
        """

        if os.environ.get(DJANGO_AUTORELOAD_ENV) != "true":
            self.stdout.write("Starting tailwind server thread.")
            command = options['tw_command']
            kwargs = {"shell": True}

            tw_thread = threading.Thread(
                target=subprocess.run, args=(command, ), kwargs=kwargs
            )
            tw_thread.start()
        super(Command, self).run(**options)
