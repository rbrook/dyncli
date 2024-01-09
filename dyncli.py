#!.venv/bin/python
import typer
import requests


### config
DEBUG = False
SERVER_URL = "http://localhost:8000"
###


client = typer.Typer()

# Create a namespace dictionary to store dynamic functions
namespace = {"debug": DEBUG, "requests": requests, "typer": typer}

# get schema for all commands and options from server
schema = requests.get(SERVER_URL + "/openapi.json", timeout=5).json()

commands = set()
paths = schema["paths"]
for path, path_info in paths.items():
    for method, method_info in path_info.items():
        if "cli_spec" in method_info:
            # this is a CLI related method
            cli_info = method_info["cli_spec"]
            cmd = cli_info["cmd"]
            if cmd in commands:
                raise Exception(
                    f"Duplicated command {cmd}! "
                    "Please contact the developers of this app."
                )
            commands.add(cmd)

            # param_keys = [i['name'] for i in method_info['parameters']]
            params = method_info["parameters"]
            func_params = ", ".join(
                [f"{p['name']}{'' if p['required'] else '=None'}" for p in params]
            )
            url_params = (
                "}&".join([f"{p['name']}=" + "{" + p["name"] for p in params]) + "}"
            )

            # create a typer command for this endpoint
            function_name = cmd.replace("-", "_")  # list-servers -> list_servers

            env_help = "EEENNNVVV"
            function_code = f"""
def {function_name}({func_params}):
    '''{cli_info['help']}'''
    if debug:
        print(f"calling endpoint {path}")
    
    url = f'''{SERVER_URL}{path}?{url_params}'''
    res = requests.{method}(url)
    if not res.ok:
        if debug:
            res.raise_for_status()
        print("Error! Server responded with code " + str(res.status_code))
    print(res.json())
"""

            # Execute the function code in the namespace
            exec(function_code, namespace)

            # Access the dynamically created function
            dynamic_function = namespace[function_name]

            # Now you can use the dynamically created function
            client.command(name=cmd)(dynamic_function)


if __name__ == "__main__":
    client()
