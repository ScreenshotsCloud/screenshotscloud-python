ScreenshotsCloud
======

Perfect Screenshots Anywhere
----------------------------

Get high quality screenshots using a real browser in seconds using our
reliable CDN backed API service.

Get an API Key to start using this fast screenshot API service at https://screenshots.cloud

Requirements
------------

Tested against Python 2.6+ and 3.2+

Installation
------------

Install via pip

.. code:: bash

    pip install screenshotscloud

Once installed you can generate screenshot urls as follows:

.. code:: python

    #!/usr/bin/python
    from screenshotscloud import ScreenshotsCloud

    screenshotscloud = ScreenshotsCloud('SCREENSHOTSCLOUD_KEY', 'SCREENSHOTSCLOUD_SECRET')

    screenshotUrl = screenshotscloud.screenshotUrl({
        "url": "bbc.com/news",
        "width": 800
    })

-------

Contact us at support@brushd.com if you have any issues or questions
about this package.
