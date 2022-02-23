FROM python:alpine
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN ln -s /usr/local/bin/veracode-dast-trigger /app/veracode_trigger_dast_scan.py