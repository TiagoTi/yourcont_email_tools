include ../.env
main:
	cat ../requirements.txt > requirements.txt &&\
	docker build --tag $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION) . &&\
	docker push $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION) &&\
	rm requirements.txt

