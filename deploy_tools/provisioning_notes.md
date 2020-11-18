Provisioning a new site
=======================

## Required packages:
* nginx
* Python3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install nginx git python3.6 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with e.g., staging.mydomain.com

## Folder structure:

Assume we gave a user account at /home/username

/home/username
|--sites
   |--DOMAIN1
   |    |--.env
   |    |--db.sqlite3
   |    |--manage.py etc
   |    |--static
   |    |--virtualenv
   |
   |--DOMAIN2
   |    |--.env
   |    |--db.sqlite3
   |    |--manage.py etc
   |    |--static
   |    |--virtualenv
   |
   |--etc
