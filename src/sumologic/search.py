import json
import requests
import datetime


class Search(object):
    """ This object does the searches against the api """

    def __init__(self, auth, api='/logs/search', **kwargs):
        """Search the logs.

        Args:
            auth (Client): Authentication object
            api (str): Api endpath
        """
        self.api = api
        self.log = auth.log
        try:
            self.url = '%s%s' % (auth.get_url(), self.api)
        except AttributeError:
            self.url = 'https://api.sumologic.com/api/v1%s' % self.api

        try:
            self.auth = auth.get_auth()
        except AttributeError:
            self.auth = auth

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
        t_options = {
            'q': criteria,
            'format': formats,
            'tz': timezone,
            'from': time_from,
            'to': time_to,
        }
        options = '&'.join(['{}={}'.format(k, v)
                            for k, v in t_options.items()])

        req = requests.get('%s?%s' %
                           (self.url, options), auth=self.auth)

        try:
            data = req.json()
        except json.decoder.JSONDecodeError:
            data = []

        return {
            'data': data,
            'response': req.status_code,
            'reason': req.reason,
        }
