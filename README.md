# Retro-CMS
OpenSource CMS

## Development environment
First clone the repository. Once cloned we have to prepare two environments.
1. Backend
2. Frontend

## Backend
Assuming python is installed (3.9.13 or higher).
Setup a virtual environment
```
python -m venv venv
```
[Activate your environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

Install the requirements **in your activated environment**
```
pip install -r requirements.txt
```
In visual studio code, you can hit **F5** with the development environment `RUN: Webserver` selected.
Outside visual studio code, you have to set the environment variable `FLASK_APP` pointing to the `webserver.py` file.

***Windows***
```
set FLASK_APP=webserver
```
***Unix***
```
export FLASK_APP=webserver
```
**Then continue**
```
flask run
```

## Frontend
> ***All commands from this point on are executed inside the frontend folder***
  ```
  cd frontend
  ```

Make sure the frontend requirements are installed. 
```
npm install
```

The frontend can be enabled with hot-reload for easy development, for a **production** build we use the command
```
npm run build
```

This build gets served by Flask.

For hot-reload run the next command along side the backend
```
npm run watch
```
