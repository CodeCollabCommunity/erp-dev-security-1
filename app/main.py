"""FastAPI app module"""
from fastapi import FastAPI
from app.api import api_router


fastapi_app = FastAPI(
    title='security microservice',
    description='security microservice API',
    # docs_url=None, # Disable docs (Swagger UI)
    # redoc_url=None, # Disable redoc
    swagger_ui_parameters={'docExpansion': 'None'}
)


@fastapi_app.get("/", status_code=200)
def healthcheck() -> dict:
    """API Healthcheck"""
    return {"Healthcheck": "Ok"}


fastapi_app.include_router(
    router=api_router,
    prefix='/api/v1'
)


# fastapi_app.mount(
#     '/statics', StaticFiles(directory=statics, html=True), name='statics'
# )
app = fastapi_app
