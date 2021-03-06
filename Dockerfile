FROM python:3.10-slim
LABEL maintainer="Lauro Gomes <laurobmb@gmail.com>"
WORKDIR /app
COPY . .
RUN python -m pip install -r requirements.txt 
EXPOSE 8080
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8080", "app:app" ]
