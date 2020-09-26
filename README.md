# flask_microservice
Create flask microservice with React
За основу взято [проект.](https://testdriven.io/courses/tdd-flask/pytest-setup/#collapse1)

**Побудова образа:**  
 - `docker-compose -f docker-compose-dev.yml build`

**Запуск контейнера:**    
- `docker-compose -f docker-compose-dev.yml up -d`  
або  
- `docker-compose -f docker-compose-dev.yml up` 

Для образа из Docker використовується порт 5001, результат знайти за адресою  
 http://localhost:5001/ping

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


