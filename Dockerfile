FROM python:alpine

COPY . /app/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/veracode_trigger_dast_scan.py"]