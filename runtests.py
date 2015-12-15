#!/usr/bin/env python

import sys
from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "django_react_filters",
            "tests",
        ],
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF="tests.urls"
    )


def runtests():
    argv = sys.argv[:1] + ["test"] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
