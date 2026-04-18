# setup server

# 1: start kernel + python
FROM python:3.12-slim-bookworm 

# 2: ENV optional to show logs
ENV PYTHONUNBUFFERED=1

# 3: update kernel + install dep
RUN apt-get update && apt-get -y install gcc libpq-dev

# 4: create project folder : kernel
WORKDIR /app

# 5: Copy req.txt
COPY requirements.txt /app/requirements.txt

# 6: install req
RUN pip install -r /app/requirements.txt

# 7: copy src code
COPY . /app/
