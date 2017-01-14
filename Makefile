TESTARGS = --cov-report term-missing --cov alkahest

help:
	@echo
	@echo "  Alkahest"
	@echo "  \033[36mtest_app\033[0m     Runs a test application at 0.0.0.0:5000"
	@echo "  \033[36mdeps\033[0m         installs and updates dependencies"
	@echo "  \033[36mdev_deps\033[0m     installs and updates dev dependencies"
	@echo "  \033[36mtest\033[0m         runs pytest"
	@echo "  \033[36mxdist\033[0m        runs pytest on 4 cores"
	@echo "  \033[36mwhl\033[0m          builds the wheel file"
	@echo "  \033[36mlint\033[0m         Runs Flake8"
	@echo

deps:
	pip install --upgrade pip setuptools
	pip install --upgrade -r requirements.txt

dev_deps:
	pip install --upgrade pip setuptools
	pip install --upgrade -r dev_requirements.txt

test:
	py.test $(TESTARGS)

test_app:
	python test_application/run_app.py

xdist:
	py.test -n 4 $(TESTARGS)

lint:
	flake8 alkahest

whl:
	python setup.py bdist_wheel

dev:
	python setup.py develop

.PHONY: deps dev_deps
