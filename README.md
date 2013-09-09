Python implemented Java `hashCode` methods.

    >>> import jhashcode
    >>> print jhashcode.hashcode('hello world')
    1794106052
    >>> print jhashcode.hashcode(u'僕と契約して、魔法少女になってほしい！')
    640953514
    >>> print jhashcode.hashcode(0)
    0

The results should be the same with Java.

Now `int`, `str` or `unicode` hash function is ready.
