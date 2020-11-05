import click

from .analysis import cli_analysis
from .generate import cli_generate


@click.group('cli')
def cli():
    pass


cli.add_command(cli_analysis)
cli.add_command(cli_generate)
