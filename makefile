bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
console:
	python main.py list
test_environment:
	@echo "This should print the email address of the user you are authenticated as:"
	curl -X POST $(SPACE_URL) -H "Authorization: Token $(FIBERY_API_TOKEN)" -H "Content-Type: application/json" -d '{"query": "{me{email}}"}'
