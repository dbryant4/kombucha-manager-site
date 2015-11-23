#!/bin/bash
set -e

docker-compose --file docker-compose-test.yml up --force-recreate -d db
docker-compose --file docker-compose-test.yml up --force-recreate web
docker-compose --file docker-compose-test.yml stop db
docker-compose --file docker-compose-test.yml rm --force -v
