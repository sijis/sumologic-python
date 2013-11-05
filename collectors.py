#!/usr/bin/python -tt

import requests


class Collectors(object):

    def __init__(self, auth, api='/collectors', **kwargs):
        self.api = api
        self.debug_mode = kwargs.get('debug', False)
        try:
            self.url = '%s%s' % (auth.get_url(), self.api)
        except AttributeError:
            self.url = 'https://api.sumologic.com/api/v1%s' % self.api

        try:
            self.auth = auth.get_auth()
        except AttributeError:
            self.auth = auth

    def set_debug(self, debug):
        self.debug_mode = debug

    def debug(self, content=None):
        if self.debug_mode:
            options = [
                'auth', 'api', 'url', 'debug_mode'
            ]
            print 'debug: search --------'
            for option in options:
                print '%s => %s' % (option, getattr(self, option))
            print 'Content: %s ' % content
            print '----------------------'

    def get_collectors(self, limit=1000, offset=0):
        options = {}
        options['limit'] = limit
        options['offset'] = offset
        request = requests.get('%s?%s' % (self.url, options), auth=self.auth)
        return request
