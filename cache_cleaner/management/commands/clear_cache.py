from django.core.cache import cache, caches
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    A Django management command to clear the cache.
    This command allows you to clear the entire cache or individual caches.

    Options:
        cache_names (list, optional): A list of one or more cache names to clear.
        --all (bool, optional): A flag to clear all defined cache backends.
    """

    help = "Clear the entire cache or individual caches."

    def _stdout_success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def _stdout_error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def add_arguments(self, parser):
        """
        Adds arguments to the command parser.

        * cache_names: A list of cache names to clear.
        * --all: A flag to clear all caches.
        """
        parser.add_argument(
            "cache_names",
            nargs="*",
            type=str,
            help="List of specific cache names to clear",
        )
        parser.add_argument(
            "--all",
            action="store_true",
            dest="clear_all",
            help="Clear all caches",
        )

    def handle(self, *args, **options):
        """
        Handles the cache clearing based on the provided arguments.

        * If `clear_all` is True, clears all defined cache backends.
        * If specific `cache_names` are provided, clears those caches if they exist.
        * If no arguments are provided, clears the default cache.
        """
        cache_names = options["cache_names"]
        clear_all = options["clear_all"]

        if clear_all:
            for cache_name in caches:
                caches[cache_name].clear()
                self._stdout_success(f"Cleared cache '{cache_name}'!")
            self._stdout_success("Cleared all caches!")

        elif cache_names:
            for cache_name in cache_names:
                if cache_name in caches:
                    caches[cache_name].clear()
                    self._stdout_success(f"Cleared cache '{cache_name}'!")
                else:
                    self._stdout_error(f"Cache '{cache_name}' does not exist!")
        else:
            cache.clear()
            self._stdout_success("Cleared default cache!")
