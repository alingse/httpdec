# coding=utf-8
from .decode import decode

import click
from StringIO import StringIO
import pyperclip
import sys


stdin = sys.stdin
stdout = sys.stdout

typed = dict(
    h='header',
    c='cookie')
types = typed.keys() + typed.values()


def fake_clip():
    content = pyperclip.paste()
    fin = StringIO(content)
    fout = StringIO()

    def close():
        value = fout.getvalue()
        pyperclip.copy(value)

    fout.close = close
    return fin, fout


def fake_raw(content):
    fin = StringIO(content)
    return fin


@click.command()
@click.option('-d', '--type', type=click.Choice(types), help='decode type')
@click.option('-p', '--clip', is_flag=True, help='read/write to clipboard')
@click.option('--raw', type=unicode, help='raw input string', default=None)
@click.argument('input', type=click.File('r'), default=stdin)
@click.argument('output', type=click.File('w'), default=stdout)
def httpdec(output, input, raw, clip, type):
    """
    httpdec [OPTIONS] [INPUT] [OUTPUT]

    INPUT: the source file, default is stdin

    OUTPUT: the output file, default is stdout
    """
    if clip:
        input, output = fake_clip()

    if raw is not None:
        input = fake_raw(raw)

    type = typed[type[0]]

    decode(input, output, type)
    input.close()
    output.close()
