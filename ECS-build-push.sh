aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 612227694518.dkr.ecr.eu-west-1.amazonaws.com
docker build -t swimming-reservation .
docker tag swimming-reservation:latest 612227694518.dkr.ecr.eu-west-1.amazonaws.com/swimming-reservation:latest
docker push 612227694518.dkr.ecr.eu-west-1.amazonaws.com/swimming-reservation:latest