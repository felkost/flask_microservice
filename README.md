# flask_microservice
Create flask microservice with React
За основу взято [проект.](https://testdriven.io/courses/tdd-flask/pytest-setup/#collapse1)

**Побудова образа:**  
 - `docker-compose -f docker-compose-dev.yml build`

**Запуск контейнера:**    
- `docker-compose -f docker-compose-dev.yml up -d`  
або  
- `docker-compose -f docker-compose-dev.yml up` 

Для образа из Docker використовується порт 5001:  
- перевірка шляху ping (отримання ынформації з OSMX) http://localhost:5001/ping  
- якщо створені тестові дані, то результа отримати через http://localhost:5001/users  
- якщо створені тестові дані, то адмін-панель відкрити через http://localhost:5001/admin/user/  
- пергляд документації за посиланням http://localhost:5001/doc/  


**Запуск та тестування кількох сервісів**  

- Щоб запустити сервіси users та users-db виконати  
`docker-compose -f docker-compose-dev.yml up -d --build`  
або (якщо контейнери вже побудовані)  
`docker-compose -f docker-compose-dev.yml up -d` 

- Щоб запустити *тестування* сервісів users та users-db виконати  
`docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests"`
- Щоб протестувати БД, потрібно  
-- перестворити БД  
`docker-compose -f docker-compose-dev.yml exec users python manage.py recreate_db`  
-- увійти в postgres  
`docker-compose -f docker-compose-dev.yml exec users-db psql -U postgres`  
-- виконати команди для перегляду структури БД в postgres  
`postgres=# \c users_dev`  
*`You are now connected to database "users_dev" as user "postgres".`*  

  `users_dev=# \dt`  
         `List of relations`  
 `Schema | Name  | Type  |  Owner  `  
`--------+-------+-------+----------  `  
 `public | users | table | postgres  `  
`(1 row)`  

  `users_dev=# \q`  

- Для зупинки сервісів виконати  
`docker-compose -f docker-compose-dev.yml down`

**Покриття кода тестами та якість коду**  
- Перевірка, яка частина коду покрита тестами (результат можна побачити в testdriven-app/services/users/htmlcov/index.html)  
`docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -p no:warnings --cov="project" --cov-report html`  
- перевірка коду на відповідність стандарту PEP8  
`docker-compose -f docker-compose-dev.yml exec users flake8 project`  
- перевірка коду на відповідність форматування файлів   
`docker-compose -f docker-compose-dev.yml exec users black project --check`  
`docker-compose -f docker-compose-dev.yml exec users black project --diff`  
`docker-compose -f docker-compose-dev.yml exec users black project`  
- перевірка коду на відповідність сортування модулів під час їх імпорту  
`docker-compose -f docker-compose-dev.yml exec users /bin/sh -c "isort project/**/*.py --check-only"`  
`docker-compose -f docker-compose-dev.yml exec users /bin/sh -c "isort project/**/*.py --diff"`  
`docker-compose -f docker-compose-dev.yml exec users /bin/sh -c "isort project/**/*.py"`  

PS:  
При появі помилок при додаванні даних в БД, останню слід перестворити:  
`docker-compose -f docker-compose-dev.yml exec users python manage.py recreate_db`  

Для додавання тестових даних виконати  
`docker-compose -f docker-compose-dev.yml exec users python manage.py seed_db`  

Для тестування використовують команди:  
- normal run   
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests"`

- disable warnings  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -p no:warnings`

- run only the last failed tests  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" --lf`

- run only the tests with names that match the string expression  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -k "config and not test_development_config"`

- stop the test session after the first failure  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -x`

- enter PDB after first failure then end the test session  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -x --pdb`

- stop the test run after two failures  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" --maxfail=2`

- show local variables in tracebacks  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" -l`

- list the 2 slowest tests  
`$ docker-compose -f docker-compose-dev.yml exec users python -m pytest "project/tests" --durations=2`  

- тестування модульних тестів (без підключення до БД)    
`docker-compose -f docker-compose-dev.yml exec users pytest "project/tests/test_users_unit.py" -p no:warnings -k "unit" -n auto`  

