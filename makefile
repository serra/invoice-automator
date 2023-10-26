bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip build
	pip install -e .
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
	
	get-paid --help
console:
	get-paid list-invoices
pdf:
	get-paid generate-pdf-for-invoices
list:
	get-paid list-invoices
emails:
	get-paid prepare-emails-for-invoices
download_stylesheets:
	wget "https://www.serraict.com/assets/themes/bootstrap/resources/bootstrap/css/bootstrap.min.css" -O ./style/css/bootstrap.min.css
	wget "https://www.serraict.com/assets/themes/bootstrap/css/style.css?v=1.1" -O ./style/css/style.css
