import re
from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class ClearCacheCommandTests(TestCase):
    def _remove_ansi_escape_codes(self, text):
        ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
        return ansi_escape.sub("", text)

    def _output_to_str(self, output):
        output_str = output.getvalue()
        output_str = self._remove_ansi_escape_codes(output_str)
        output_str = output_str.strip()
        return output_str

    def _call_command(self, *args, **kwargs):
        output = StringIO()
        error = StringIO()
        call_command(
            "clear_cache",
            *args,
            stdout=output,
            stderr=error,
            **kwargs,
        )
        output_str = self._output_to_str(output)
        error_str = self._output_to_str(error)
        return (output_str, error_str)

    def test_without_args(self):
        out, _ = self._call_command()
        self.assertEqual(out, "Cleared default cache!")

    def test_with_all_arg(self):
        out, _ = self._call_command(all=True)
        self.assertEqual(
            out,
            "Cleared cache 'default'!\n"
            "Cleared cache 'cache_1'!\n"
            "Cleared cache 'cache_2'!\n"
            "Cleared cache 'cache_3'!\n"
            "Cleared all caches!",
        )

    def test_with_valid_cache_names_args(self):
        out, _ = self._call_command("default", "cache_1", "cache_3")
        self.assertEqual(
            out,
            "Cleared cache 'default'!\n"
            "Cleared cache 'cache_1'!\n"
            "Cleared cache 'cache_3'!",
        )

    def test_with_invalid_cache_names_args(self):
        _, err = self._call_command("unknown")
        self.assertEqual(err, "Cache 'unknown' does not exist!")
