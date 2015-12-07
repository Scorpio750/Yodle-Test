class Juggler:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]

	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2]) + " | Preferences:" + str(self.preferences)

	def addPreferences(self,preferences):
		self.preferences = preferences

	def dotProduct(self, circuit, circuits):
		dotProduct = 0
		
		for c in circuits:
			if c.name == circuit:
				found = c

		for i in range(len(self.HEP)):
			dotProduct += int(self.HEP[i]) * int(found.HEP[i])
		return dotProduct
