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

The frontend needs to be compiled, assuming you are a developer, you might want to use hot-reload.
Open a new terminal, and `cd ./frontend/cms` into the CMS folder.

If this is a fresh git clone, consider installing the dependencies first.
```
yarn install
```
> You can also use: `npm install`

If you have installed the dependencies, use the following command for hot-reload
```
yarn watch
```
> You can also use `npm run watch`

For a production build, recommended is to run the following command
```
yarn build
```
> You can also use `npm run build`

There is no need to worry about where the files will be build, they will be put into the right location for you to use.
Python (flask) is what serves the frontend to the consumer. Even if you would make use of hot-reload, so make sure your python environment is running and setup correctly.

> NOTE: yarn has to be available for the application itself. You cannot fully utilize this application if `yarn` is not available as a global system environment variable.

### Swagger

The backend contains 3 different swagger pages for you to use.
- http://127.0.0.1:5000/devs
- http://127.0.0.1:5000/docs
- http://127.0.0.1:5000/swagger-ui

Those pages contain information on all the different endpoints available to you. Endpoints located here are in active use by the frontend. However, you could utilize those endpoints for yourself to make your own app!

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

---
# Advanced Topics
[This section is specifically written for contributors / developers which would like to read more about how the internals work.](.github/docs/index.md)