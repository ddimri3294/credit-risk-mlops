FROM python:3.8

RUN pip3 install --no-cache scikit-learn pandas joblib flask requests boto3 tabulate sagemaker-training

COPY training_script.py /usr/bin/train

RUN chmod 755 /usr/bin/train

## define training_script.py as the script entry point
#ENV SAGEMAKER_PROGRAM train.py

EXPOSE 8080
