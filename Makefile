all:
	docker build -t cpro29a/ddemo_gettweets .
clean:
	docker rmi cpro29a/ddemo_gettweets

