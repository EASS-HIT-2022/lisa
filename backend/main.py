from fastapi import FastAPI, Body, Depends, HTTPException
from app.model import EventSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
import app.handlers as handlers

app = FastAPI()


@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}


@app.get("/events", tags=["events"])
async def get_events():
    try:
        events = handlers.get_events()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Unable to get events: {err}")

    return {"data": events}


@app.post("/events", dependencies=[Depends(JWTBearer())], tags=["events"])
def create_event(event: EventSchema):
    try:
        handlers.create_event(event)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Unable to create event: {err}")

    return {"data": "event created."}


@app.post("/auth/signup", tags=["auth"])
async def create_user(user: UserSchema = Body(...)):
    try:
        handlers.create_user(user)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Unable to create user: {err}")

    return sign_jwt(user.email)


@app.post("/auth/login", tags=["auth"])
async def user_login(user: UserLoginSchema = Body(...)):
    if not handlers.is_user_exists(user):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return sign_jwt(user.email)


# @app.get("/events/{id}", tags=["events"])
# def get_single_event(id: int):
#     if ........:
#         return {
#             "error": "No such event with the supplied ID."
#         }
#
#     TODO: return event with the given id
#
