run:
	docker run -d -p 3333:80 -v script:/devops_volume --rm --name test test:v2
start:
	docker exec -it test:v2 bash  