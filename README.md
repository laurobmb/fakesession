# fakesession

[![Docker Repository on Quay](https://quay.io/repository/lagomes/fastapicookie/status "Docker Repository on Quay")](https://quay.io/repository/lagomes/fastapicookie)

    curl -c - http://127.0.0.1:8080/cookie/

Para coletar os cookies:

    curl -c - http://url-da-aplciacao

para efetuar as chamadas com o cookie:

    curl -b 'nome_do_cookie=valor' http://url-da-aplicacao