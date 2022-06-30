import click

from partner_tools.cli.controller import run_register_device, run_configure


@click.group(help="Partner Tools CLI - Tool for interacting with the Microsoft Partner Center")
def run():
    pass  # Shows help text, nothing to do


@run.command(help='Register device in Autopilot')
def register_device():
    run_register_device()


@run.command(help='Configure authentication')
def configure():
    run_configure()


def main():
    try:
        run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
