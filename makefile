packages:
	@pip install -r requirements.txt

make-venv:
	@python3 -m venv venv

start-venv:
	@source venv/bin/activate

stop-venv:
	@deactivate

run:
	@python main.py
