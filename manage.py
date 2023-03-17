#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os,dotenv
import sys


def main():

    if not os.path.exists('.env'):
        raise FileExistsError(".env file not found..")
    dotenv.load_dotenv()

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
