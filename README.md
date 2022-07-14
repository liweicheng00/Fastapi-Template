# Setup

```bash
pip install -r requirements.txt
```
# Local Run
```bash
# Run MongoDB, Redis and Docker image
docker build -t backend .
docker-compose up

# Run localhost
python run.py
```
# Test
```bash
export RUNTIME_ENV=test
pytest --cov=app --cov-report term-missing

# Load test
k6 run k6/script.js
```