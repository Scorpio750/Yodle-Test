class Circuit:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]

	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2])
