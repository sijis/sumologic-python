#!/usr/bin/python -tt

import requests
import datetime


class Search(object):
    """ This object does the searches against the api """

    def __init__(self, auth, api='/logs/search', **kwargs):
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
            print 'debug: search --------'
            for option in options:
                print '%s => %s' % (option, getattr(self, option))
            print 'Content: %s ' % content
            print '----------------------'

    def query(self, criteria, **opts):
        """ Returns a dict of the query, including the results
            :param critera: string of search criteria
            :param **opts:
                :formats: json/xml (default: json)
                :timezone: timezone to use (default: UTC)
                :time_from: 15m ago from now (datetime)
                :time_to: right now (datetime)
        """
        time_now = datetime.datetime.now().replace(second=0, microsecond=0)
        right_now = time_now.isoformat()
        minutes_ago = (time_now - datetime.timedelta(minutes=15)).isoformat()

        formats = opts.get('formats', 'json')
        timezone = opts.get('timezone', 'UTC')
        time_from = opts.get('time_from', minutes_ago)
        time_to = opts.get('time_to', right_now)

        # setting up options
        t_options = []
        t_options.append('q=%s' % criteria)
        t_options.append('format=%s' % formats)
        t_options.append('tz=%s' % timezone)
        t_options.append('from=%s' % time_from)
        t_options.append('to=%s' % time_to)
        options = '&'.join(t_options)

        req = requests.get('%s?%s' % (self.url, options), auth=self.auth)
        data = {}
        data['data'] = req.json()
        data['response'] = req.status_code
        data['reason'] = req.reason
        return data
