import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line
    argv = ['manage.py']
    argv.append(os.path.basename(sys.argv[0]))
    argv.extend(sys.argv[1:])
    execute_from_command_line(argv)