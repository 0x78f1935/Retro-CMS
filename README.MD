# Retro - All in One CMS

This CMS aims to provide the most straight forward all-in-one retro solution for educational purpose only.

## None provided Requirements
- Database
- Emulator

It's recommended to host this in production with Docker. If this repo has no docker files yet, no stress.
This repository is actively under development, the final phase of the project will be the docker environment.
The build in webserver provided by flask is not suitable for a production environment.

## Development

When your intention is to work on this repository, the build in webserver provided by flask, is enough to help you get started.
Setup your Python **3.9** or higher environment, either virtual or globally and install the requirements.
```sh
pip install -r requirements.txt
```

If you just cloned this repository, you might want to untrack the `.env` file.
```
git update-index --assume-unchanged .env
```

If you would like to track the `.env` file again, run `git update-index --no-assume-unchanged .env` \
Now, open the `.env` file and make sure the configuration is configured correctly based on your setup.

### Database

Before you can start the application, you have to create/populate the database. This application comes with some cli shortcuts.
To use those shortcuts, you have to set the environment variable `FLASK_APP` in the terminal you want to access those commands.
Make the variable point to the file `webserver.py`.

For example, on windows:
```
set FLASK_APP=webserver.py
```

On unix:
```
export FLASK_APP=webserver.py
```

you can now feed **flask** the `--help` command to get a overview of available commands.

If you just cloned this repository **fresh**, execute the next few commands:
```
flask db init
flask db migrate
flask db upgrade
flask system init
```
> Note: Your `.env` file has to be configured correctly in order for this to succeed

If everything is finished, you should be able to run `flask run` to start the webserver. In visual studio code, you can select `RUN: Flask` from the debug dropdown and hit F5 instead.

### Frontend

The frontend needs to be compiled on every change, however, at this moment there is no frontend, so don't worry about it.

### Swagger

The backend contains 3 different swagger pages for you to use.
- http://127.0.0.1:5000/devs
- http://127.0.0.1:5000/docs
- http://127.0.0.1:5000/swagger-ui

### Character Renderer

To render characters, we use [nitro-imager](https://github.com/billsonnn/nitro-imager) internally.
This is a server on it's own which you are required to start before characters are able to load correctly.
Before the imager works, you are required to have the assets downloaded and converted. This can be done within the CMS.

Once you have the assets downloaded and converted, for local development, just start `docker-compose.yaml`
```
docker-compose up --build imager
```
By adding `-d` you detach the terminal from docker once the container has started. Feel free to use this option if you would like to keep using your terminal.

---
# Credits
## [Credit where credit is due](.github/docs/CREDITS.MD)!
