username=$1
passwd=$2

curl --location --request POST 'http://localhost:8000/api/token/' \
--header 'Authorization: Token 074e044e42e409a3434ddc65895d114b3c87ebe1' \
--form 'username=$username' \
--form 'password=$passwd'

 curl --location --request POST 'http://ec2-3-17-14-98.us-east-2.compute.amazonaws.com:8000/api/token/' \
 --form 'username=$username' \
 --form 'password=$passwd'
