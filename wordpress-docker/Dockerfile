FROM debian:jessie
RUN apt-get -y update && apt-get -y upgrade
RUN  DEBIAN_FRONTEND=noninteractive apt-get -y install nginx mariadb-server-10.0 curl vim php5-fpm unzip php5-mysql net-tools netcat

RUN curl -o /var/www/latest.zip https://wordpress.org/latest.zip && unzip -o -d /var/www/ /var/www/latest.zip && rm -r /var/www/html &&  mv /var/www/wordpress /var/www/html
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

RUN service mysql start && sleep 3 && mysql -e 'create database wordpress;' &&  mysql -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');"

COPY ./nginx-default /etc/nginx/sites-available/default
COPY ./wp-config.php /var/www/html/wp-config.php

EXPOSE 80
CMD service mysql restart && service php5-fpm restart && service nginx restart && tail -F /var/log/nginx/access.log
