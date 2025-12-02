test : venv
	source venv/bin/activate && python3 gen_keys.py

venv :
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

clean :
	rm -rf venv
