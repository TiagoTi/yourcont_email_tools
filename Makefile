include .env
main:
	@env
run:
	gunicorn  --bind 0.0.0.0:8088 wsgi:app

worker-run:
	celery -A tasks worker

coverter_css:
	cd tools && node css-file-to-inline.js

pyclean:
    # find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

dockerup_dev:
	docker-compose -f docker-compose.yaml -f docker-compose-network.yaml up -d

template:
	bin/find_and_change.sh
template-dev:
	bin/find_and_change.sh dev