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

> !Important: For hot-reload to work properly; First run the frontend followed by the backend

# Interfaces
If everything runs correctly, the following links should be available
- [Frontend](http://127.0.0.1:5000/)
- [RapiDocs](http://127.0.0.1:5000/devs)
- [Redocly](http://127.0.0.1:5000/devs)
- [Swagger](http://127.0.0.1:5000/swagger-ui)


## Environment
For this to work correctly, you are required to make a `.env` file in the root of this repository.
You can use the following `.env` file as example:
```
DB_USERNAME=root
DB_PASSWORD=SuperSecretPass123
DB_HOST=127.0.0.1
DB_PORT=3888
DB_SCHEMA=retro
```
