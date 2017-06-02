# urlparse in python3 has been renamed to urllib.parse
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import hmac
import hashlib

class ScreenshotsCloud:
	def __init__(self, apiKey, apiSecret, defaultPrefix = 'https://api.screenshots.cloud/'):
		self.apiKey = apiKey
		self.apiSecret = apiSecret
		self.defaultPrefix = defaultPrefix

	def screenshotUrl(self, options):
		parameters = urlencode(options)
		hmacToken = hmac.new(str.encode(self.apiSecret), str.encode(parameters), hashlib.sha1)
		return "%sv1/screenshot/%s/%s?%s" % (self.defaultPrefix, self.apiKey, hmacToken.hexdigest(), parameters)
