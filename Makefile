install_dependencies:
	pip install -r requirements.txt

local_test:
	uvicorn src.app.main:app --port 8000 --log-level debug --reload
