from sumologic import Client, Search
from unittest.mock import patch, MagicMock

CLIENT = Client(auth=('username', 'password'),
                debug=True)


@patch('requests.get')
def test_get_collectors(requests_get):
    search = Search(CLIENT)
    requests_get.return_value = MagicMock(status_code=200, reason='test_cases')
    requests_get.return_value.json.return_value = {}
    results_data = {'data': {}, 'response': 200, 'reason': 'test_cases'}
    assert search.query(criteria='test') == results_data


def test_init_auth_and_url_exceptions():
    auth_mock = MagicMock(auth=('u', 'p'))
    auth_mock.get_url.side_effect = AttributeError
    auth_mock.get_auth.side_effect = AttributeError
    search = Search(auth=auth_mock)
    assert search.url.startswith('https://api.sumologic.com/api')
