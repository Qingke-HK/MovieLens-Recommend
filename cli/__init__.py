import click

from .analysis import cli_analysis
from .generate import cli_generate
from .download import cli_download


@click.group('cli')
def cli():
    pass


cli.add_command(cli_analysis)
cli.add_command(cli_generate)
cli.add_command(cli_download)
