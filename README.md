# Fakesession FastAPI

[![Docker Repository on Quay](https://quay.io/repository/lagomes/fastapicookie/status "Docker Repository on Quay")](https://quay.io/repository/lagomes/fastapicookie)

### Build
	podman build -t fakesession .

### Run 
	podman run -it --rm --name fastapi -p8080:8080 fakesession

### get cookie
	curl -c - http://127.0.0.1:8080/cookie/

#### Para coletar os cookies:
	curl -c - http://url-da-aplciacao

#### para efetuar as chamadas com o cookie:
	curl -b 'podhostnamesession=check_my_new_cookie' http://url-da-aplciacao:8000/read

### read cookie
	curl -c - http://127.0.0.1:8080/read

