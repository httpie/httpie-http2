"""
HTTP/2 transport plugin for HTTPie.

"""
from httpie.plugins import TransportPlugin
from hyper.contrib import HTTP20Adapter


__version__ = '0.0.1'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD'


class HTTP2TransportPlugin(TransportPlugin):

    name = 'HTTP/2 transport'
    prefix = 'https://'

    def get_adapter(self):
        return HTTP20Adapter()
