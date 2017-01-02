import requests


class Collectors(object):
    """ This object acts upon the collectors """

    def __init__(self, auth, api='/collectors', **kwargs):
        """Access sumologic Collectors.

        Args:
            auth (Auth): Authentication object
            api (str): Api endpath
        """
        self.api = api
        self.collector_id = None
        self.log = auth.log

        try:
            self.url = '%s%s' % (auth.get_url(), self.api)
        except AttributeError:
            self.url = 'https://api.sumologic.com/api/v1%s' % self.api

        try:
            self.auth = auth.get_auth()
        except AttributeError:
            self.auth = auth

    def get_collectors(self, limit=1000, offset=0):
        """Returns a dict of collectors.

        Args:
            limit (int): number of collectors to return
            offset (int): the offset of where the list of collectors should begin from
        """
        options = {}
        options['limit'] = limit
        options['offset'] = offset
        request = requests.get(self.url, params=options, auth=self.auth)

        try:
            results = request.json()['collectors']
        except KeyError:
            results = request.json()

        return results

    def find(self, name):
        """Returns a dict of collector's details if found.

        Args:
            name (str): name of collector searching for
        """
        collectors = self.get_collectors()

        for collector in collectors:
            if name.lower() == collector['name'].lower():
                self.collector_id = collector['id']
                return collector

        return {'status': 'No results found.'}

    def delete(self, id=None):
        """Delete a collector from inventory.

        Args:
            id (int): id of collector (optional)
        """
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
        """Return a dict of collector.

        Args:
            id (int): id of collector (optional)
        """
        cid = self.collector_id
        if id:
            cid = id

        url = '{0}/{1}'.format(self.url, cid)
        request = requests.get(url, auth=self.auth)
        return request.json()

    def get_id(self):
        """Return the collector's id"""
        return self.collector_id
