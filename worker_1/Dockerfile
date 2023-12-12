FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    mysql-server \
    python3-pip

RUN pip3 install pymysql cryptography==3.4.8


RUN service mysql start \
    && mysql -e "CREATE DATABASE jenkins_database;" \
    && mysql -e "CREATE USER 'jenkins_user'@'localhost' IDENTIFIED BY 'password';" \
    && mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'jenkins_user'@'localhost';" \
    && mysql -e "FLUSH PRIVILEGES;"


EXPOSE 3306

CMD ["mysqld"]
