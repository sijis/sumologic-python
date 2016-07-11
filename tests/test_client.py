import sumologic


def test_client_get_auth():
    client = sumologic.Client(auth=('check', 'password'))
    assert client.get_auth() == ('check', 'password')


def test_client_get_url():
    client = sumologic.Client(auth=('u', 'p'), domain='api.example.com')
    assert client.get_url() == 'https://api.example.com/api/v1'
