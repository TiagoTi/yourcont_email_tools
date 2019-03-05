run:
	gunicorn  --bind 0.0.0.0:8088 wsgi:app

coverter_css:
	cd tools && node css-file-to-inline.js

pyclean:
    # find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete