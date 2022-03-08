FROM ubi8/python-39:latest
LABEL maintainer="Lauro Gomes <laurobmb@gmail.com>"
WORKDIR /app
COPY . .
RUN python -m pip install -r requirements.txt 
EXPOSE 8080
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8080", "app:app" ]
