.. image:: https://travis-ci.org/sijis/sumologic-python.svg?branch=master
    :target: https://travis-ci.org/sijis/sumologic-python

sumologic-python
================

Sumologic's python api library

The library currently supports the following features:

* search
* collectors

.. code-block:: python

    from sumologic import Client, Collectors, Search

    # Need a client to authenticate to service
    client = Client(auth=('username', 'password'))

    # collector usage
    collector = Collectors(client)
    for c in collector.get_collectors():
        print('{0}:{1}'.format(c['name'], c['alive']))

    # find and delete a collector
    c = collector.find('logserver')
    c.delete()

    # search usage
    search = Search(client)
    results = search.query('log1', formats='json')
    print(results)

To see the library in use, go to sumologic-cli_ repo.

.. _sumologic-cli: https://github.com/sijis/sumologic-cli
