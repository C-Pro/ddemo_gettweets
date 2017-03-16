FROM cpro29a/ddemo_pybase

MAINTAINER Sergey Melekhin <sergey@melekhin.me>

ADD get_tweets.py /var/www/
WORKDIR /var/www

CMD ["python", "get_tweets.py"]

