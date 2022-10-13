FROM python:latest
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/veracode_trigger_dast_scan.py && ln -s /app/veracode_trigger_dast_scan.py /usr/local/bin/veracode-dast-trigger
ENTRYPOINT ["/bin/bash"]
