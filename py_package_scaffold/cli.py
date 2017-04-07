#!/usr/bin/env python

from getpass import getuser

import click

from .package_scaffold import create_package


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is not None:
        pass

    location = click.prompt('Package location:', type=str)
    name = click.prompt('Package name:', type=str)
    package_url = click.prompt('Package url:', type=str)
    description = click.prompt('Description:', type=str)
    author_email = click.prompt('Author email:', type=str)
    license = click.prompt('License:', type=str)
    author = getuser()

    extra_args = {}
    extra_key = 'start'
    while extra_key:
        extra_key = click.prompt('Extra key', type=str, default='')
        if extra_key:
            extra_val = click.prompt('Extra val', type=str)
            extra_args[extra_key] = extra_val

    extra_args.update({
        'package_url': package_url,
        'description': description,
        'author_email': author_email,
        'license': license,
        'author': author
    })

    create_package(
        location,
        name,
        extra_args
    )


if __name__ == '__main__':
    cli()
