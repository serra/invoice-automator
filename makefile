bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
help:
	@echo "Available commands:"
	@echo "  bootstrap: Create a virtual environment and install dependencies."
	@echo "  update: Update dependencies."
	@echo "  help: Show this help message."
	@echo "  console: Run the console application."
	@echo "  pdf: Generate PDFs for all invoices."
	@echo "  test_environment: Test the Fibery API connection."
	@echo "  "
	
	python main.py --help
console:
	python main.py list-invoices
pdf:
	python main.py generate-pdf-for-invoices
list:
	python main.py list-invoices
test_environment:
	@echo "This should print the email address of the user you are authenticated as:"
	curl -X POST $(SPACE_URL) -H "Authorization: Token $(FIBERY_API_TOKEN)" -H "Content-Type: application/json" -d '{"query": "{me{email}}"}'
