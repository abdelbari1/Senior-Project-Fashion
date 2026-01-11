# Introduction 
This repo is for fashion python 

# Getting Started
1.	Download and Install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html) 
2. Create a new conda environement
```
conda create -n fashion python=3.9
```
3.	Activate the environemnt 
```
conda activate fashion
```
4.	Install Depedencies
```
pip install -r requirements.in
```
5. the file (.vscode/launch.json) define a Run Config. It enables the debugging (or not) of the fashion application

# IDE 
We will be using VS Code [Download](https://code.visualstudio.com/) and we will use Python Extension [Here](https://marketplace.visualstudio.com/items?itemName=ms-python.python
)

You can use the defined Conda Environment in VS Code from the bottom bar or refer to this guide [here](https://code.visualstudio.com/docs/python/environments#_conda-environments)

# Run Locally
```
uvicorn main:app --reload
```

# References
1. FastAPI [here](https://fastapi.tiangolo.com/tutorial/)
2. Pydantic [here](https://pydantic-docs.helpmanual.io/usage/models/)
3. psycopg (https://www.psycopg.org/)
4. postgresql (15.1.1) db server (https://www.postgresql.org/)

# Build and Test
Freeze dependencies 
```
pip install pip-tools

pip-compile --upgrade --output-file=requirements.txt requirements.in
```

# Build and run image locally
`docker build . -t opus/briefcase:local --no-cache`
```
docker run -p 8000:80 -e CLOUD_AUTH="" -e CLOUD_ID="" -e MONGO_URL="" -e SENDGRID_APIKEY="" --name fashion-local --rm -d opus/fashion:local
```

# Run latest image locally 
```
docker run -p 8000:80 -e CLOUD_AUTH="" -e CLOUD_ID="" -e MONGO_URL="" -e SENDGRID_APIKEY="" --name fashion-latest --rm -d fashion.azurecr.io/opus/fashion:latest
```