#!/usr/bin/python
from screenshotscloud import ScreenshotsCloud

screenshotscloud = ScreenshotsCloud('[apiKey]', '[apiSecret]')

print screenshotscloud.screenshotUrl({
    "url": "bbc.com/news",
    "width": 800
})