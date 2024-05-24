# Use an official Python runtime as a parent image
FROM python:3.10-slim

RUN mkdir /app
WORKDIR /app

RUN mkdir -p /inputs 
RUN mkdir -p /outputs

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

ENV OUTPUT_DIR="/outputs/"

ADD hello.py /app/hello.py
# Run the script when the container launches
ENTRYPOINT ["python3", "-u", "/app/hello.py"]  # Replace with your script name and IPFS link if static, or handle args in entrypoint
