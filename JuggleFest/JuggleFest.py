import sys, numpy

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

class Circuit:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]

	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2])

def main():
	fs = open('juggletest.txt')
	jugglers, circuits = [], []

	# builds the lists of jugglers and circuits
	for line in fs:
		# construct circuits
		if line[0] == 'C':
			name = 'C' + line[3: line.find[' ', 4]]
			H = line[line.index('H') + 2]
			E = line[line.index('E') + 2]
			P = line[line.index('P') + 2]
			lastCircuit = Circuit(H, E, P, name)
			circuits.append(lastCircuit)
			print lastCircuit

		# construct jugglers
		elif line[0] == 'J':
			name = 'J' + line[3]
			H = line[line.index('H') + 2]
			E = line[line.index('E') + 2]
			P = line[line.index('P') + 2]
			lastJuggler = Juggler(H, E, P, name)

			# grabs substring of preferences from substring in original line
			preference_line = line[line.find('C'):]
			split_circuits = preference_line.split(',')

			# removes the escapekeys from the last circuit string
			last_split = split_circuits[len(split_circuits)-1]
			split_circuits[len(split_circuits)-1] = last_split.rstrip('\r\n');

			# converts list of split circuits into dict,
			# where key is the circuit and value is the dot product
			dots = [lastJuggler.dotProduct(c, circuits) for c in split_circuits]
				
			# zips these two lists into a dict
			preferences = dict(zip(split_circuits, dots))

			lastJuggler.addPreferences(preferences)
			jugglers.append(lastJuggler)
			print lastJuggler 

	# now the real fun begins


main()
