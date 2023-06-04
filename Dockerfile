FROM python:latest

WORKDIR /app

# Install kubectl in Docker image
RUN apt-get update && apt-get install -y apt-transport-https gnupg2 curl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

COPY kodem_home_assignment.py .

ENTRYPOINT ["python", "kodem_home_assignment.py"]
