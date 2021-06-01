git

    git add . 
    git pull origin master
    git commit -m "some commit"
    git push origin master
    git rm -r --cached .
How to install Mysql?

    https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04
    CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
My Config

Create file my.cnf in the project and edit this file
    
    [client]
    database = mydatabase
    user = your_username
    password = password
    default-character-set = utf8

Django

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python manage.py migrate



Run the collectstatic management command:

    python manage.py collectstatic

Go through each of your projects apps migration folder and remove everything inside, except the __init__.py file.

    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

Install mysql in pip! If you have error when installing mysqlclient

    sudo apt-get install python3-dev
    sudo apt-get install python3-dev libmysqlclient-dev
    pip install mysqlclient
    or 
    sudo apt-get install libssl-dev
    pip install mysqlclient

Статичный локализация

    django-admin compilemessages
    django-admin.py makemessages -a       