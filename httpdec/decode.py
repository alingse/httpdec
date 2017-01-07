# coding=utf-8
import json


def decode_header(content):
    headers = {}

    lines = content.split('\n')
    lines = filter(lambda x: x and ':' in x, lines)

    for line in lines:
        key, value = line[1:].split(':', 1)
        key = line[0] + key
        headers[key.strip()] = value.strip()

    content = json.dumps(headers, indent=1)
    return True, content


def decode_cookie(content):
    cookies = {}

    lines = content.split(';')
    lines = filter(None, lines)

    for line in lines:
        key, value = line.split('=', 1)
        cookies[key.strip()] = value.strip()

    content = json.dumps(cookies, indent=1)
    return True, content


def decode(input, output, type_):
    content = input.read()
    if type_ == 'header':
        func = decode_header
    elif type_ == 'cookie':
        func = decode_cookie
    else:
        func = lambda x: (True, x) # NOQA

    status, out = func(content)
    output.write(out)
    output.write('\n')
    return status
