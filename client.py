#!/usr/bin/python -tt

import requests
import datetime


class Client(object):

    def __init__(self, auth, **kwargs):
        self.auth = auth
        self.protocol = kwargs.get('protocol', 'https')
        self.domain = kwargs.get('domain', 'api.sumologic.com')
        self.api = kwargs.get('api', '/api/v1')
        api_path = '%s/logs/search' % self.api

        self.url = '%s://%s%s' % (self.protocol, self.domain, api_path)
        self.debug_mode = kwargs.get('debug', False)

    def set_debug(self, debug):
        self.debug_mode = debug

    def debug(self, content=None):
        if self.debug_mode:
            options = [
                'auth', 'protocol', 'domain', 'api', 'url', 'debug_mode'
            ]
            for option in options:
                print '%s => %s' % (option, getattr(self, option))
            print 'Content: %s ' % content

    def search(self, criteria, **opts):

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

        self.debug(options)

        req = requests.get('%s?%s' % (self.url, options), auth=self.auth)
        data = {}
        data['data'] = req.json()
        data['response'] = req.status_code
        data['reason'] = req.reason
        return data
