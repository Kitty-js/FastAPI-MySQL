from fastapi import FastAPI

from routes.user import user

app = FastAPI(
        title="Users REST API",
        description="A Simple REST API (CRUD) Using FastAPI and MySQL",
        version="0.0.1",
        openapi_tags=[{
                "name": "users",
                "description": "users routes"
        }]
)

app.include_router(user)