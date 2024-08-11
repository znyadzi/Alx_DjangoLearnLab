#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys
import os

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as erImport:
        raise ImportError(
            "Django Import Error"
            "Make sure Django is added to your Environment variables and try again"
            "If you are using pycharm, you should "
        ) from erImport
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
