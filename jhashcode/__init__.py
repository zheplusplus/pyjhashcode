def _unknown_hash(_):
    raise TypeError('Unsupported type')


def hash_str_unicode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


def hash_int(i):
    return i

_TP_MAPPING = {
    str: hash_str_unicode,
    unicode: hash_str_unicode,
    int: hash_int,
}


def hashcode(o):
    return _TP_MAPPING.get(type(o), _unknown_hash)(o)
