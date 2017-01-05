# coding=utf-8
from .decode import decode

import click
import pyperclip
import sys

if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO

stdin = sys.stdin
stdout = sys.stdout


def fake_clip():
    content = pyperclip.paste()
    fin = StringIO(content)
    fout = StringIO()

    def close():
        value = fout.getvalue()
        pyperclip.copy(value)

    fout.close = close
    return fin, fout


@click.command()
@click.option('-h', '--header', is_flag=True, help='decode the header')
@click.option('-c', '--cookie', is_flag=True, help='decode the cookie')
@click.option('-p', '--clip', is_flag=True, help='read/write to clipboard')
@click.argument('input', type=click.File('r'), default=stdin)
@click.argument('output', type=click.File('w'), default=stdout)
def httpdec(output, input, clip, cookie, header):
    """
    httpdec [OPTIONS] [INPUT] [OUTPUT]

    INPUT: the source file, default is stdin

    OUTPUT: the output file, default is stdout

    NOTE:

        1. `-h` or `-c` must specific one
    """

    if clip:
        input, output = fake_clip()

    if not header and not cookie:
        click.echo('`-h` `-c` must specific one')

    decode(input, output, header, cookie)
