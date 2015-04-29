# Kombucha Manager

A Django app which will help keep track of Kombucha brews and bottling.

## Description


## Requirements

- Django 1.8
- every package in `requirements.txt`
- PosgreSQL server

## Getting Started

```
pip install -r requirements.txt
python manage.py migrate

```

## Tests


## Dump Updated Data
```
DATABASE_URL='postgres://bucha:br00klyn@127.0.0.1/mysite' /usr/bin/python /vagrant/manage.py dumpdata > provision/files/data.json
```

## Generate Model Graphs

Ensure [Graphviz](http://graphviz.org) is installed.

```
python manage.py graph_models -a -g -o kombucha_manager_visualized.png

```