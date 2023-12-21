help:
	@echo "Available commands:"
	@echo "  bootstrap: Create a virtual environment and install dependencies."
	@echo "  update: Update dependencies."
	@echo "  help: Show this help message."
	@echo "  pdf: Generate PDFs for all invoices."
	@echo "  test_environment: Test the Fibery API connection."
	@echo "  "
	
	get-paid --help
### Development commands
bootstrap:
	python -m venv venv
	mkdir -p ./output
	mkdir -p ./output/specs	
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip build
	python -m pip install -r requirements-dev.txt
	pip install -e .
	wkhtmltopdf --version # Check that wkhtmltopdf is installed
check-environment:
	robot --outputdir output/specs ./docs/api_access.rst
specs:
	robot --outputdir output/specs ./docs/*.rst
test:
	pytest
test-and-watch:
	watchmedo shell-command --patterns="*.py" --recursive --command='clear; pytest' .
download_stylesheets:
	wget "https://www.serraict.com/assets/themes/bootstrap/resources/bootstrap/css/bootstrap.min.css" -O ./style/css/bootstrap.min.css
	wget "https://www.serraict.com/assets/themes/bootstrap/css/style.css?v=1.1" -O ./style/css/style.css
### Build and release commands
build:
	python -m build
release:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "There are uncommitted changes or untracked files"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then \
		echo "Not on main branch"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse HEAD)" != "$$(git rev-parse origin/main)" ]; then \
		echo "Local branch is ahead of origin"; \
		exit 1; \
	fi
	@git tag v$$(python -m setuptools_scm --strip-dev)
	@git push origin --tags
docker_image:
	docker build -t invoice-automator .
docker_run:
	docker run --env-file=.env -p 5001:5000 invoice-automator
### Commands for the get-paid CLI
pdf:
	get-paid generate-pdf-for-invoices
list:
	get-paid list-invoices
emails:
	get-paid prepare-emails-for-invoices
