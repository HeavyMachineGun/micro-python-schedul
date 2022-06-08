FROM jupyter/base-notebook
WORKDIR /jupyter
COPY ./src ./src
WORKDIR /jupyter/notebooks
COPY ./jupyter/notebooks .
COPY requirements.txt requirements.txt
RUN ipython profile create 
RUN pip install -r requirements.txt