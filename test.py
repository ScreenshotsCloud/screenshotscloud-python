from screenshotscloud import ScreenshotsCloud

def test_screenshotscloud():
	screenshotscloud = ScreenshotsCloud('my-key-generated-at-screenshots-dot-cloud', 'mysecretstringgeneratedatscreenshotsdotcloud')
	return screenshotscloud.screenshotUrl({
	    "url": "bbc.com/news"
	})

def test_answer():
	assert test_screenshotscloud() == 'https://api.screenshots.cloud/v1/screenshot/my-key-generated-at-screenshots-dot-cloud/3fc4e5cd418052343e3dc61b2eaf17bec53adaeb?url=bbc.com%2Fnews'