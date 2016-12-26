import click

import scritps


@click.group()
def cli():
    pass


@cli.command()
def naming_issue():
    scritps.naming_issue()


if __name__ == '__main__':
    cli()
