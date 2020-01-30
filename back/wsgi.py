"""
In production, entry point of the wsgi server (setup in uwsgi.ini)
"""

from app import create_app

app = create_app()