"""
Для запуска скрипта (локально, не из Dockerfile) необходимо:
1) перейти в каталог testdriven-app/services/users
2) export FLASK_APP=project/__init__.py
3) export FLASK_DEBUG=1
4) выполнить  python manage.py run
результат открыть в браузере http://localhost:5000/users/ping
PS: для образа из Docker используется порт 5001, поэтому результ открыть по адресу http://localhost:5001/users/ping
"""
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User  # без этой строки не пересоздается БД в 'recreate_db'

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='michael', email="hermanmu@gmail.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()


if __name__ == '__main__':
    cli()
