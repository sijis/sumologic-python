#!/usr/bin/python -tt

import requests


class Collectors(object):
    """ This object acts upon the collectors """

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
        """ Enables or disables debug mode
            :param debug: boolean (True/False)
        """
        self.debug_mode = debug

    def debug(self, content=None):
        """ Print out the values of class variables
            :param content: contents to print out
        """
        if self.debug_mode:
            options = [
                'auth', 'api', 'url', 'debug_mode'
            ]
            print 'debug: collector -----'
            for option in options:
                print '%s => %s' % (option, getattr(self, option))

            if content:
                print 'Content: %s ' % content
            print '----------------------'

    def get_collectors(self, limit=1000, offset=0):
        """ Returns a dict of collectors
            :param limit: number of collectors to return
            :param offset: the offset of where the list of
                           collectors should begin from
        """
        options = {}
        options['limit'] = limit
        options['offset'] = offset
        request = requests.get(self.url, params=options, auth=self.auth)

        try:
            return request.json()['collectors']
        except KeyError:
            return request.json()

    def find(self, name):
        """ Returns a dict of collector's details if found
            :param name: name of collector searching for
        """
        collectors = self.get_collectors()

        for collector in collectors:
            if name.lower() == collector['name'].lower():
                return collector

        return {'status': 'No results found.'}
