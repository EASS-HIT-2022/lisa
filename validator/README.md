# Validator
LISA project is here to help us manage and save the important events in our life.

We can sign-in (create our own user), login to LISA system get all the events and create new ones

## Environment variables
Should be the same as the backend database values:

Mongo database name:
```DB_NAME="lisa"```

Mongo port:
```DB_PORT="27017"```

Mongo host:
```DB_HOST="localhost"```

## Validate events
This MS runs every 12AM and marks out dated events. 

Event that its date has passed will be marked with active=False
