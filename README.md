Python implemented Java `hashCode` methods.

    >>> import jhashcode
    >>> print jhashcode('hello world')
    1794106052
    >>> print jhashcode.hashcode(u'僕と契約して、魔法少女になってほしい！')
    640953514

The results should be the same with Java.

Now `str` or `unicode` hash function is ready.
