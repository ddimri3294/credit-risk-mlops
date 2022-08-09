FROM python:3.8

RUN pip3 install --no-cache scikit-learn pandas joblib flask requests boto3 tabulate sagemaker-training

COPY train.py /opt/ml/code

RUN chmod 755 /opt/ml/code

# define train.py as the script entry point
ENV SAGEMAKER_PROGRAM train.py

EXPOSE 8080
