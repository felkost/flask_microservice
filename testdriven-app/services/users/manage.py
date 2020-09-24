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
from project import app, db

cli = FlaskGroup(app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
