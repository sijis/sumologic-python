import logging
from .utils import get_logging_level

class Client(object):
    """ This object autheticates the account to the api """

    def __init__(self, auth, **kwargs):
        """
        Initializes Client object.

        Args:
            auth (Auth): Authentication object
            api (str): Api endpath
        """
        self.auth = auth
        self.protocol = kwargs.get('protocol', 'https')
        self.domain = kwargs.get('domain', 'api.sumologic.com')
        self.api = kwargs.get('api', '/api/v1')
        api_path = '%s' % self.api
        self.url = '%s://%s%s' % (self.protocol, self.domain, api_path)

        # setup debug logging
        self._debug_mode = kwargs.get('debug', False)
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.StreamHandler())
        self.log.setLevel(get_logging_level(self._debug_mode))

    def get_url(self):
        """ Returns full api url """
        return self.url

    def get_auth(self):
        """ Returns api auth details """
        return self.auth
