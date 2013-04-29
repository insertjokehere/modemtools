
class device():

	PORTFORWARD = "portforward"

	def __init__(self, url):
		self.baseUrl = url
		self._authProvider = None

	def basicDetect(self, page):
		return False

	def deepDetect(self):
		return False

	def versionDetect(self):
		return False

	def setAuthProvider(self, provider):
		self._authProvider = provider