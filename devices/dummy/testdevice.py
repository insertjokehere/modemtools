import modemtools

class testdevice(modemtools.device):

	def __init__(self):
		super.__init__("http://example.com")

	def basicDetect(self, page):
		return True

	def deepDetect(self):
		return True

	def versionDetect(self):
		return True