# Base image
FROM python:3.6.1-alpine
# define the present working directory
WORKDIR /flask_dogan
# copy the contents into the working dir
ADD . /flask_dogan
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","merge_kodum.py"]
