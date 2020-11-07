#!/bin/bash
# Tested using bash version 4.1.5
for ((i=1;i<=10000;i++)); 
do 
  curl -H "Content-Type: application/json" -X POST -d  '{"firstname": "Terry", "lastname": "Fuckwit", "postcode": "ND $1 UQ"}'  http://localhost:8000/heroes/
  echo $i
done
