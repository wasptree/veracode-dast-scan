# Veracode DAST Scan
<!-- ABOUT THE PROJECT -->
## About This Project

veracode_dast_scan is a python script to aid with submiting Veracode DAST analaysis through the Veracode API.

The script will accept your Veracode API ID and API Key as parameters, along with the name of an existing DAST analysis profile to start.

The DAST analysis will be scheduled to run immediately. You can also optionally specify the maxium duration of the scan with the -duration switch (default 24 hours) 


<!-- GETTING STARTED -->
## Getting Started

**Docker**:

A pre-built amd64 image of veracode-dast-scan image containing the dependencies and python script is available on docker hub [hub.docker.com/veracode-dast-scan](https://hub.docker.com/repository/docker/wasptree/veracode-dast-scan)

Alternatively build a local image from this repository:

  ```sh
    $ git clone https://gitlab.com/wasptree/veracode-dast-scan
    $ cd veracode-dast-scan
    $ docker build -t veracode-dast-scan .
  ```

**Python Script**:

There is a packaged version of the python script, including the required dependencies in a "vendor" directory.
This can be downloaded as a zip and executed. Please note the PYTHONPATH should be updated to include the vendor directory.
Python3 is required to run the script.

<!-- SETUP -->
## Setup

The script requires a valid Veracode API ID and Key, for authentication with the Veracode platform. 
This ID and KEY can be generated for your specific Veracode platform user, or for a service account.
From the Veracode platform, select your user account and generate API Credentials.

<!-- USAGE EXAMPLES -->
## gitlab-ci Examples

The following Gitlab CI Job is utilising the pre-built docker image to schedule a DAST analysis to run immediately

Checkout the .gitlab-ci.yml file in this project for a complete Veracode SCA + SAST + DAST analysis workflow example.

**Pre-built docker image**:
```
veracode_dast_scan:
    image: wasptree/veracode-dast-scan
    stage: dast_scan
    script:
      - veracode-dast-scan -vid ${VERACODE_API_ID} -vkey ${VERACODE_API_KEY} -scan my_dast_analysis
```

**Python release package:**

Alternatively, you can download the python script and dependencies in the release package. This Requires an image/runner that has Python3 installed. This could then be added to an existing step as a post build action.
```
veracode_dast_scan:
    image: python:latest
    stage: dast_scan
    script:
      - wget https://gitlab.com/wasptree/veracode-dast-scan/-/archive/latest/veracode-dast-scan-latest.zip
      - unzip veracode-dast-scan-latest.zip && cd veracode-dast-scan-latest
      - export PYTHONPATH=`pwd`/veracode_libs && chmod +x ./veracode_dast_scan.py
      - ./veracode_dast_scan.py -vid ${VERACODE_API_ID} -vkey ${VERACODE_API_KEY} -scan my_dast_analysis
```



<!-- To Do -->
## To Do

1. Provide additional options for creating new DAST analysis profiles.
2. Add ISM support
