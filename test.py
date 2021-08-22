from screenshotscloud import ScreenshotsCloud

def test_screenshotscloud():
	screenshotscloud = ScreenshotsCloud('my-key-generated-at-screenshots-dot-cloud', 'mysecretstringgeneratedatscreenshotsdotcloud')
	return screenshotscloud.screenshotUrl({
	    "url": "openai.com/research",
		"user_agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36"
	})

def test_answer():
	assert test_screenshotscloud() == 'https://api.screenshots.cloud/v1/screenshot/my-key-generated-at-screenshots-dot-cloud/3fc4e5cd418052343e3dc61b2eaf17bec53adaeb?url=bbc.com%2Fnews'