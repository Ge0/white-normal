"""Entry point."""

import click

from . import hello
from .__about__ import __version__


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
def main():
    """Run a (fake) VideoHub server."""
    click.echo(hello())


if __name__ == '__main__':
    main()
