from screenshotscloud import ScreenshotsCloud

def test_screenshotscloud():
	screenshotscloud = ScreenshotsCloud('my-key-generated-at-screenshots-dot-cloud', 'mysecretstringgeneratedatscreenshotsdotcloud')
	return screenshotscloud.screenshotUrl({
	    "url": "maps.google.com"
	})

def test_answer():
	assert test_screenshotscloud() == 'https://api.screenshots.cloud/v1/screenshot/my-key-generated-at-screenshots-dot-cloud/20bc07c6b9d6875ddce3d7b69dbacac3c0ca3c7a?url=maps.google.com'