#!/usr/bin/python -tt


class Client(object):

    def __init__(self, auth, **kwargs):

        self.auth = auth
        self.protocol = kwargs.get('protocol', 'https')
        self.domain = kwargs.get('domain', 'api.sumologic.com')
        self.api = kwargs.get('api', '/api/v1')
        api_path = '%s/logs/search' % self.api

        self.url = '%s://%s%s' % (self.protocol, self.domain, api_path)
        self.debug = kwargs.get('debug', False)

        self.set_debug(self.debug)

    def set_debug(self, debug):
        if debug:
            options = [
                'auth', 'protocol', 'domain', 'api', 'url', 'debug'
            ]
            for option in options:
                print '%s => %s' % (option, getattr(self, option))
