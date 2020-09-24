# flask_microservice
Create flask microservice with React

**Побудова образа:**  
 - docker-compose -f docker-compose-dev.yml build


**Запуск контейнера:**    
- docker-compose -f docker-compose-dev.yml up -d  
або  
- docker-compose -f docker-compose-dev.yml up 

Для образа из Docker використовується порт 5001, результат знайти за адресою  
 http://localhost:5001/users/ping

PS:
Для запуска скрипта (не з контейнера) виконати:  
1) перейти в каталог testdriven-app/services/users
2) export FLASK_APP=project/__init__.py
3) export FLASK_DEBUG=1
4) запустити скрипт python manage.py run
результат відкрити в браузері http://localhost:5000/users/ping