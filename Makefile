# Name of the Docker image and container
IMAGE_NAME=employee-attrition-api
CONTAINER_NAME=attrition-service

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop the Docker container
stop:
	docker stop $(CONTAINER_NAME)

# Remove the Docker container
remove:
	docker rm $(CONTAINER_NAME)

# View logs from the container
logs:
	docker logs $(CONTAINER_NAME)

# Rebuild image and restart fresh
restart: stop remove build run

# Show running containers
ps:
	docker ps

# Clean up: stop, remove container and image
clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME) || true

# Help
help:
	@echo "Available targets:"
	@echo "  build   - Build the Docker image"
	@echo "  run     - Run the Docker container"
	@echo "  stop    - Stop the Docker container"
	@echo "  remove  - Remove the Docker container"
	@echo "  logs    - Show container logs"
	@echo "  restart - Stop, remove, build, and run fresh container"
	@echo "  ps      - List running containers"
	@echo "  clean   - Remove container and image"
