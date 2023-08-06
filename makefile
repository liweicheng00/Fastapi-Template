
depends:
	pip install --upgrade pip && pip install -r app/requirements.txt && pip install -r tests/requirements.test.txt


test:
	pytest