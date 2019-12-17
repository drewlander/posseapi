FROM python:3-slim
WORKDIR /usr/src/app

COPY web/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "web/app.py" ]
