```
>>> import chunks
>>> from StringIO import StringIO

>>> decoded = StringIO()

>>> input = """25\r\nThis is the data in the first chunk\r\n\r\n1C\r\nand this is the second one\r\n\r\n3\r\ncon\r\n8\r\nsequence\r\n0\r\n\r\n"""

>>> for chunk in chunks.decode(StringIO(input)):
>>>     decoded.write(chunk)

>>> decoded.seek(0)
>>> print decoded.getvalue()
This is the data in the first chunk
and this is the second one
consequence
```