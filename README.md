# dyncli
An example of a generic CLI which builds itself dynamically around an existing FastAPI backend endpoints.

This work is based on a [lecture](https://ep2023.europython.eu/session/designing-a-human-friendly-cli-for-api-driven-infrastructure) given by Oliver Rew at EuroPython 2023.

It has been modified in order to utilise Typer's rich CLI capabilities.

## Instructions
In order to start the local server, install the requirements using "pip" and then run
> uvicorn server.app:app --reload

Then open a new terminal and run
> pip install .

Assuming everything worked, you can run
> dcli --help

to see the Typer help message, available commands etc.


*You can - of course - skip the local installation of `dcli` call directly:
  > python dyncli.py --help
