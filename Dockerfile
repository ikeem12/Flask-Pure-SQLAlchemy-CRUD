FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENV DOCKERIZE_VERSION=v0.9.3

ENV DOCKER_DB_URL=mysql+pymysql://root:root123@db:3306/prueba_sqlalchemy

RUN wget https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz \
    && rm dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]