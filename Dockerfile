# get image
FROM python:3.10-slim

# set working directory
WORKDIR /app

# copy files to working directory
COPY . /app

# install dependencies
RUN pip install -r /app/requirements.txt

# this manage command provides reload, perhaps not required in all environments
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8888", "--reload"]
