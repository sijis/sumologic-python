#!/usr/bin/python -tt

class Client(object):

    def __init__(self, auth, **kwargs):
        self.auth = auth
        self.protocol = kwargs.get('protocol', 'https')
        self.domain = kwargs.get('domain', 'api.sumologic.com')
        self.api = kwargs.get('api', '/api/v1')
        api_path = '%s' % self.api
        self.url = '%s://%s%s' % (self.protocol, self.domain, api_path)
        self.debug_mode = kwargs.get('debug', False)

    def set_debug(self, debug):
        self.debug_mode = debug

    def debug(self, content=None):
        if self.debug_mode:
            options = [
                'auth', 'protocol', 'domain', 'api', 'url', 'debug_mode'
            ]
            print 'debug ----------------'
            for option in options:
                print '%s => %s' % (option, getattr(self, option))
            print 'Content: %s ' % content
            print '----------------------'

    def get_url(self):
        return self.url

    def get_auth(self):
        return self.auth
