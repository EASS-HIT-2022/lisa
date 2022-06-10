# LISA
LISA project is here to help us manage and save the important events in our life.

We can sign-in (create our own user), login to LISA system get all the events and create new ones

## Environment variables
JWT secret: 
```SECRET="c56bc63929a8edffc060"``` - To create a secret do: import secrets; secrets.token_hex(10)

algorithm:
```ALGORITHM=HS256```

Mongo database name:
```DB_NAME="lisa"```

Mongo port:
```DB_PORT="27017"```

Mongo host:
```DB_HOST="localhost"```

## Create user
POST ```/user/signup``` - will create user in lisa environment.

body example:
```json
{
  "fullname": "Niv Hamisha",
  "email": "niv@email.com",
  "password": "password"
}
```

## User login
POST ```/user/login``` - will authorize the already signed-in user and return a valid JWT token

body example:
```json
{
  "email": "niv@email.com",
  "password": "password"
}
```
## Get events
GET ```/events``` - will return all lisa events

## Create event
POST ```/events``` - will create event in lisa environment

body example:
```json
{
  "title": "Fanjoya",
  "organizer_email": "niv@email.com",
  "date": "24.5.2022",
  "description": "student's summer party"
}
```
