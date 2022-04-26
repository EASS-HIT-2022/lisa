from pydantic import BaseModel, Field, EmailStr


class EventSchema(BaseModel):
    title: str = Field(...)
    organizer_email: str = Field(...)
    date: str = Field(...)
    description: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "title": "Fanjoya",
                "organizer_email": "niv@email.com",
                "date": "24.5.2022",
                "description": "student's summer party"
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Niv Hamisha",
                "email": "niv@email.com",
                "password": "password"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "niv@email.com",
                "password": "password"
            }
        }
