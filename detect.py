
class deviceDetector():

	def __init__(self, url, username=None, password=None, ignoreVersion=False, deviceName=None):
		self._ignoreVersion = ignoreVersion
		self._url = url
		self._username = username
		self._password = password
		self._deviceName = deviceName

	def detect(self):
		return []

	def getAllDevices(self):
		return []

	def getDevice(self, name):
		return None