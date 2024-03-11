"""
This app is an exmaple app showing how to build an API that feeds its client CLI
"""
import fastapi
import pydantic


class EndpointCLISpec(pydantic.BaseModel):
    cmd: str
    # formatters: Optional[list[CLIFormatter]] # TODO
    help: str


class Router(fastapi.APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, *args, cli: EndpointCLISpec = None, **kwargs):
        return super().api_route(
            *args,
            methods=["GET"],
            openapi_extra={"cli_spec": cli.model_dump()},
            **kwargs,
        )

    def post(self, *args, cli: EndpointCLISpec = None, **kwargs):
        return super().api_route(
            *args,
            methods=["POST"],
            openapi_extra={"cli_spec": cli.model_dump()},
            **kwargs,
        )

    def delete(self, *args, cli: EndpointCLISpec = None, **kwargs):
        return super().api_route(
            *args,
            methods=["DELETE"],
            openapi_extra={"cli_spec": cli.model_dump()},
            **kwargs,
        )


cli_router = Router()
