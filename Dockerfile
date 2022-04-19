FROM python:latest


ADD passcheck.py .


CMD [ "python", "./passcheck.py" ]

