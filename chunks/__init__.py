import re

def from_pattern(pattern, type, *args):
    def coerce(value):
        value = str(value)
        match = pattern.search(value)
        if match is not None:
            return type(match.group(1), *args)
        raise ValueError('unable to coerce "%s" into a %s' % (value, type.__name__))
    return coerce

to_int = from_pattern(re.compile('([-+]?[0-9]+)', re.IGNORECASE), int)
to_hex = from_pattern(re.compile('([-+]?[0-9A-F]+)', re.IGNORECASE), int, 16)
to_float = from_pattern(re.compile('([-+]?[0-9]*\.?[0-9]+)'), float)
to_megabytes = lambda n: n * 1024 * 1024

def encode(fileobj, chunk_limit=to_megabytes(0.5)):
    while True:
        value = fileobj.read(int(chunk_limit))
        bytes = len(value)
        if bytes:
            yield '%x\r\n' % bytes
            yield '%s\r\n' % value
        else:
            yield '0\r\n'
            yield '\r\n'
            return

def decode(fileobj, chunk_limit=to_megabytes(1)):
    while True:
        index = fileobj.readline(len('%x' % chunk_limit))

        if not index:
            raise EOFError('unexpected blank line')

        length = to_hex(index)

        if length > chunk_limit:
            raise OverflowError('invalid chunk size of "%d" requested, max is "%d"' % (length, chunk_limit))

        value = fileobj.read(length)

        assert len(value) == length

        yield value

        tail = fileobj.read(2)

        if not tail:
            raise ValueError('missing \\r\\n after chunk')

        assert tail == '\r\n', 'unexpected characters "%s" after chunk' % tail

        if not length:
            return
