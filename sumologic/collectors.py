#!/usr/bin/python -tt

import requests


class Collectors(object):
    """ This object acts upon the collectors """

    def __init__(self, auth, api='/collectors', **kwargs):
        self.api = api
        self.debug_mode = kwargs.get('debug', False)
        self.collector_id = None

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
                self.collector_id = collector['id']
                return collector

        return {'status': 'No results found.'}


    def delete(self, id=None):
        ''' Delete's a collector from inventory
            Returns ...
            :param id: id of collector (optional)
        '''
        cid = self.collector_id

        if id:
            cid = id

        # param to delete id
        url = '{0}/{1}'.format(self.url, cid)
        request = requests.delete(url, auth=self.auth)
        try:
            # unable to delete collector
            response = request.json()
        except ValueError:
            # returns when collector is deleted
            # apparently, the request does not return
            # a json response
            response = {
                        u'message': u'The request completed successfully.',
                        u'status': 200,
                    }
        return response


    def info(self, id):
        ''' Returns a dict of collector
            :param id: id of collector (optional)
        '''
        cid = self.collector_id
        if id:
            cid = id

        url = '{0}/{1}'.format(self.url, cid)
        request = requests.get(url, auth=self.auth)
        return request.json()

    def get_id(self):
        return self.collector_id
