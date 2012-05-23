import unittest

from StringIO import StringIO
import string
import chunks
import itertools

def chrs(start, end):
    return (chr(o) for o in xrange(ord(start), ord(end) + 1))

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

testdata_in = string.join(chrs('a', 'z'), ':')
testdata_out = [
    '4\r\n',
    'a:b:\r\n',
    '4\r\n',
    'c:d:\r\n',
    '4\r\n',
    'e:f:\r\n',
    '4\r\n',
    'g:h:\r\n',
    '4\r\n',
    'i:j:\r\n',
    '4\r\n',
    'k:l:\r\n',
    '4\r\n',
    'm:n:\r\n',
    '4\r\n',
    'o:p:\r\n',
    '4\r\n',
    'q:r:\r\n',
    '4\r\n',
    's:t:\r\n',
    '4\r\n',
    'u:v:\r\n',
    '4\r\n',
    'w:x:\r\n',
    '3\r\n',
    'y:z\r\n',
    '0\r\n',
    '\r\n'
]


class TestChunks(unittest.TestCase):
    def test_wikipedia_entry(self):
        decoded = StringIO()
        encoded = StringIO()

        input = """25\r\nThis is the data in the first chunk\r\n\r\n1C\r\nand this is the second one\r\n\r\n3\r\ncon\r\n8\r\nsequence\r\n0\r\n\r\n"""
        output = """This is the data in the first chunk\r\nand this is the second one\r\nconsequence"""

        for chunk in chunks.decode(StringIO(input)):
            decoded.write(chunk)

        decoded.seek(0)

        for chunk in chunks.encode(decoded):
            encoded.write(chunk)

        decoded = StringIO()
        encoded.seek(0)

        for chunk in chunks.decode(StringIO(input)):
            decoded.write(chunk)

        self.assertEqual(output, decoded.getvalue())

    def test_encode(self):
        fileobj = StringIO(testdata_in)

        for found, expected in zip(chunks.encode(fileobj, chunk_limit=4), testdata_out):
            self.assertEqual(found, expected)
    
    def test_decode(self):
        fileobj = StringIO(string.join(testdata_out, ''))

        for found, expected in zip(list(chunks.decode(fileobj)), (string.join(o, '') for o in grouper(4, testdata_in, ''))):
            self.assertEqual(found, expected)

