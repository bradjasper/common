"""
    Taken from pytechd at http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
"""

class Enum(object):
    """This is used for creating real enumerated choice fields in django or for
    other use"""

    def __init__(self, dict_entries=None, **entries):
        if dict_entries:
            self.__dict__.update(dict_entries)
        if entries:
            self.__dict__.update(entries)

    def __repr__(self):
        args = ["%s=%s" % (k, repr(v)) for (k, v) in vars(self).items()]
        return "Enum(%s)" % ", ".join(args)

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__.get(key)
        else:
            raise AttributeError

    def __radd__(self, other):
        if isinstance(other, list):
            return other + list(self)

    def __add__(self, other):
        if isinstance(other, list):
            return list(self) + other

    def __iter__(self):
        return self.__dict__.iteritems()

