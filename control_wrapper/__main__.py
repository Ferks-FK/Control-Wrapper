import sys
from control_wrapper import version
from importlib import metadata
from aiohttp import __version__
from platform import uname
from argparse import ArgumentParser, Namespace

def show_version() -> None:
    entries = []

    entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
    entries.append('- Control_Wrapper v{0.major}.{0.minor}.{0.micro}-{0.release}'.format(version))
    if version.release != "final":
        new_version = metadata.version('control_wrapper')

        if new_version:
            entries.append('- Control_Wrapper MetaData v{0}'.format(new_version))
    
    entries.append('- AioHttp v{0}'.format(__version__))
    plataform_uname = uname()
    entries.append('- System Info: {0.system} {0.release} {0.version}'.format(plataform_uname))
    print('\n'.join(entries))

def core(parser: ArgumentParser, args: Namespace) -> None:
    if args.version:
        show_version()
    else:
        parser.print_help()

def parse_version():
    parser = ArgumentParser(prog="control_wrapper", description="Shows the version of lib Control_Wrapper.")
    parser.add_argument('-v', '--version', action="store_true", help='Show the library version.')
    parser.set_defaults(func=core)

    return parser, parser.parse_args()

def main() -> None:
    parser, args = parse_version()
    args.func(parser, args)

if __name__ == '__main__':
    main()