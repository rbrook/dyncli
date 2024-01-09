"""
This module is an example of a FastAPI backend providing info for the CLI
You can run it by running:
> uvicorn server.app:app --reload
"""
import fastapi

from .router import cli_router, EndpointCLISpec


app = fastapi.FastAPI()


@cli_router.get(
    "/entries",
    summary="Retrieve existing entries",
    cli=EndpointCLISpec(cmd="get-entry", help="Get existing entry"),
)
def list_entries(name: str, day: str = "today"):
    return {"message": f"Hello, {name}! Today is {day}"}


@cli_router.post(
    "/entries",
    summary="Create a new entry",
    cli=EndpointCLISpec(cmd="post-entry", help="Create an entry"),
)
def enter(name: str = "client"):
    return {"message": f"Hello, {name}! You just POSTED to this endpoint!"}


# you can toggle this to see how the command dis/appear on the CLI side
@cli_router.get(
    "/bye",
    summary="Goodbye summary",
    cli=EndpointCLISpec(cmd="gbye", help="say goodbye"),
)
def index_get(name: str = "client"):
    return {"message": f"Goodbye, {name}!"}


app.include_router(cli_router)
