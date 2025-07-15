.PHONY : lock, run, build

# --------------------------
# Automation Tasks with Makefile
# --------------------------

# --------------------------
# Generate the Poetry Lockfile
# --------------------------
lock:
	@echo "Starting the lock process ..."
	@python3 -m pip install -q poetry==1.8.3
	@poetry lock

# --------------------------
# Running the Web Scraper
# --------------------------
project-init:
	@echo "Starting the firestore information ..."
	@poetry install
	@poetry run python src/firestore_init.py

# --------------------------
# Execução da Inferência
# --------------------------
run:
	@echo "Starting the Inference ..."
	@poetry install
	@poetry run python src/water_scan_main.py

# --------------------------
# Automações para o docker
# --------------------------

# Nome da imagem Docker
IMAGE_NAME=water-scan-app

# === Comandos ===

## Build da imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

docker-run:	
	docker run --rm $(IMAGE_NAME)

## Remove imagem Docker (limpeza)
clean:
	docker rmi $(IMAGE_NAME) || true

## Rebuild completo (limpa e recria)
rebuild: clean build


