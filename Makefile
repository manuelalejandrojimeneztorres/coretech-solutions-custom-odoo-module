build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

backup:
	bash scripts/backup.sh

restore:
	bash scripts/restore.sh
