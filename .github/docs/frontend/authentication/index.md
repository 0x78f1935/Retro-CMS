# Authentication

The frontend requires to talk to the backend in order to fully function, which should make sense.
For the frontend to talk with the backend an `access_token` is required. This `access_token` expires by default every **15** min.

```
┌──────────────┐POST /api/v1/users/login  ┌──────────────┐
│Vue           │{ username, password }    │Server        │
├──────────────┼─────────────────────────►├──────────────┤
│User          │Returns {                 │Authenticate  │
│Login         │  access / refresh token }│Create tokens │
└───────┬──────┘◄─────────────────────────┼──────────────┤
        │                                 │              │
┌───────▼──────┐                          │              │
│Access        │request data with access  │              │
│Resource      │token in header as bearer ├──────────────┤
│with          ├─────────────────────────►│Validate token│
│Expired Token │Returns 401               │Throws 401    │
├──────────────┤◄─────────────────────────┼──────────────┤
├──────────────┤POST/api/v1/users/refresh │              │
│              │{ refresh_token }         ├──────────────┤
│              ├─────────────────────────►│              │
│Token Refresh │return new {              │Verify        │
│              │  access / refresh token }│refresh token │
│              │◄─────────────────────────┤              │
└───────┬──────┘                          └──────────────┘
        │
┌───────▼──────┐
│Access        │
│Resource      │
│with          │
│New Token     │
└──────────────┘
```

## First User

If the project has no users, the very first user created will assign itself the **"owner"** role.
Someone with the **"owner"** role **can execute unsigned code**, ***cannot*** be removed, and has a lot more benefits which are significant
different then someone with an **admin** role. Keep this in mind. This system will never create unwanted users on its own.

## Groups / Scope

At this moment, there are only 3 scopes. This document has been written **23-12-2022**.
There might be more scopes / groups available in the future, for now we have:

| Name    	| Function                                                                      	| Obtained By                                                                                                                                                                                                                                     	|
|---------	|-------------------------------------------------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `guest` 	| Can play the game                                                             	| The guest role / scope is the default role / scope all accounts obtain simply by creating a new account.                                                                                                                                        	|
| `admin` 	| Can play the game, can play police in the game, can update assets             	| This moment in time there is no official way to assign admin role.                                                                                                                                                                              	|
| `owner` 	| Can play the game, can setup assets, configure cms, can execute unsigned code 	| The very first user created through the CMS will obtain this role. Check out the `FLASK_APP` **--help** command. There might be a command available which creates users without the needs to go through the CMS. For now this is not available. 	|

## Access Token

An `access_token` is required to talk with the backend and authenticate as an user.

**POST** `/api/v1/users/login`

```
{
    email*: string
            E-mail address of the userConstraints: Max 500 chars
    password*: string
            Hold the status of the password of the userConstraints: Max 64 chars
}
```
After successful authentication a new SSO ticket will be generated. Returns access and refresh token.
```
{
    access_token*: string
        Authorization token which allows request to the backend
    refresh_token: string
        Authorization Refresh token
}
```
> ! The following links only work if the backend is running on port 5000

- See [rapidoc](http://127.0.0.1:5000/devs#post-/api/v1/users/login)
- See [redoc](http://127.0.0.1:5000/docs#tag/Users/paths/~1api~1v1~1users~1login/post)
- See [swagger-ui](http://127.0.0.1:5000/swagger-ui)

## Refresh Token

The `access_token` is valid by default for **15** min after which the token expires.
After the expiration time, the `access_token` expires and stops working. The `refresh_token` can be utilized to obtain a new `access_token`.

**POST** `/api/v1/users/refresh`

Instead of the `access_token` as bearer token, provide the `refresh_token`.
After successful authentication this returns a new access and refresh token.
```
{
    access_token*: string
        Authorization token which allows request to the backend
    refresh_token: string
        Authorization Refresh token
}
```

For more info check out open-api specs:

> ! The following links only work if the backend is running on port 5000

- See [rapidoc](http://127.0.0.1:5000/devs#post-/api/v1/users/refresh)
- See [redoc](http://127.0.0.1:5000/docs#tag/Users/paths/~1api~1v1~1users~1refresh/post)
- See [swagger-ui](http://127.0.0.1:5000/swagger-ui)
