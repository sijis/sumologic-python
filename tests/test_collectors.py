from sumologic import Client, Collectors
from unittest.mock import patch, MagicMock

CLIENT = Client(auth=('username', 'password'),
                debug=True)


@patch('requests.get')
def test_get_collectors(requests_get):
    collector = Collectors(CLIENT)

    requests_get.return_value.json.return_value = {}
    assert collector.get_collectors() == {}


@patch('sumologic.Collectors.get_collectors', return_value={})
def test_find_no_collectors(collectors_mock):
    collector = Collectors(CLIENT)
    find_collector = collector.find('missing_collector')
    assert 'status' in find_collector


@patch('sumologic.Collectors.get_collectors')
def test_find_collectors(collectors_mock):
    collector = Collectors(CLIENT)
    collectors_mock.return_value = [
        {'name': 'Found', 'id': 100}
    ]
    find_collector = collector.find('found')
    assert 'id' in find_collector


def test_get_id():
    collector = Collectors(CLIENT)
    assert collector.get_id() is None


@patch('requests.get')
def test_info(requests_get):
    collector = Collectors(CLIENT)
    requests_get.return_value.json.return_value = {}
    assert collector.info(1) == {}


@patch('requests.delete')
def test_delete_collector_ok(requests_delete):
    collector = Collectors(CLIENT)
    requests_delete.return_value.json.return_value = {}
    assert collector.delete(1) == {}


@patch('requests.delete')
def test_delete_collector_notok(requests_delete):
    collector = Collectors(CLIENT)
    requests_delete.return_value.json.side_effect = ValueError
    assert 'message' in collector.delete(1)
