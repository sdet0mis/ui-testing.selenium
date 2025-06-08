#!/bin/bash

set -e

java -jar grid/selenium-server-4.33.0.jar hub & \
java -jar grid/selenium-server-4.33.0.jar node --hub http://localhost:4444 & \
GRID="grid" BROWSERS=${1} pytest -n ${2:-auto} --reruns 2 --alluredir=allure-results
