#!/bin/bash

set -e

java -jar grid/selenium-server-4.33.0.jar hub & \
java -jar grid/selenium-server-4.33.0.jar node --hub http://localhost:4444 & \
pytest -n ${1:-auto} --lf --alluredir=allure-results