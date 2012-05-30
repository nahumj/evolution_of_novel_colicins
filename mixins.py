"""
Useful Mixins for common behavior
"""

import copy


class Equalable(object):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


class Printable(object):
    def __repr__(self):
        return "<{} dict={}>".format(self.__class__.__name__, self.__dict__)


class Duplicatable(object):
    def duplicate(self):
        return copy.deepcopy(self)
