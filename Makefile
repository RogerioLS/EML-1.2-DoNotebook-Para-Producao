GREEN = "\033[32;1m"
RED = "\033[31;1m"
CYAN = "\033[36;1;3;208m"
WHITE = "\033[37;1;4m"
COLOR_LIMITER = "\033[0m"

all: build

build:
	docker build -t modelo:churn .
	@echo $(CYAN)" ------------------------------------------ "$(COLOR_LIMITER)
	@echo $(CYAN)"| Docker build whit created successfully!! |"$(COLOR_LIMITER)
	@echo $(CYAN)" ------------------------------------------ "$(COLOR_LIMITER)

run:
	docker run -d -p 5000:5000 --rm --name modelo-churn-container modelo:churn
	@echo $(CYAN)" ---------------------------------------- "$(COLOR_LIMITER)
	@echo $(CYAN)"| Docker run whit created successfully!! |"$(COLOR_LIMITER)
	@echo $(CYAN)" ---------------------------------------- "$(COLOR_LIMITER)

publish:
	docker tag modelo:churn rogeriols/modelo:churn
	docker push rogeriols/modelo:churn
	@echo $(CYAN)" -------------------------------------------------- "$(COLOR_LIMITER)
	@echo $(CYAN)"| Docker image successfully published to Docker Hub |"$(COLOR_LIMITER)
	@echo $(CYAN)" -------------------------------------------------- "$(COLOR_LIMITER)

test:
	python sources/app/test_api.py

doci:
	docker images
	docker ps

doccs:
	docker container stop modelo-churn-container

docip:
	docker image prune -a

doc_run_it:
	docker run -it modelo:churn

.PHONY: build run doci doccs docip doc_run_it