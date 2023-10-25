bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	wkhtmltopdf --version # Check that wkhtmltopdf is installed
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
emails:
	python main.py prepare-emails-for-invoices
download_stylesheets:
	wget "https://www.serraict.com/assets/themes/bootstrap/resources/bootstrap/css/bootstrap.min.css" -O ./style/css/bootstrap.min.css
	wget "https://www.serraict.com/assets/themes/bootstrap/css/style.css?v=1.1" -O ./style/css/style.css
