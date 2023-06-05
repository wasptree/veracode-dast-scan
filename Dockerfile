FROM python:latest
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/veracode_dast_rescan.py && ln -s /app/veracode_dast_rescan.py /usr/local/bin/veracode-dast-rescan
ENTRYPOINT ["/bin/bash"]
