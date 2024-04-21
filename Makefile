install_dependencies:
	pip install -r requirements.txt

local_test:
	uvicorn src.app.main:app --port 8000 --log-level debug --reload

alembic_autogenerate_revision:
	@echo "Please enter a message for the review:"
	@read MESSAGE; \
	rev_id=$$(date -u +"%Y%m%d%H%M%S"); \
	alembic -c ./src/alembic.ini revision --autogenerate -m "$$MESSAGE" --rev-id="$$rev_id"

alembic_history:
	alembic -c ./src/alembic.ini history

alembic_upgrade:
	alembic -c ./src/alembic.ini upgrade head

alembic_downgrade:
	alembic downgrade -1

docker_build_local:
	docker build -t atam .

docker_run_local:
	docker run --env PORT=8000 -p 8000:8000 atam
