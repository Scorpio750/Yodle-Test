# Yodle Jugglefest Challenge
# author @Patrick Wu

import sys, numpy
from sys import argv
from collections import OrderedDict

# Classes
class Juggler:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]

	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2]) + " | " + str(self.preferences) + " | " + str(self.scores)

	def addLists(self, preferences, scores):
		self.preferences = preferences
		self.scores = scores

	def dotProduct(self, circuit, circuits):
		dotProduct = 0
		found = match(circuits, circuit)
		# print found

		for i in range(len(self.HEP)):
			dotProduct += int(self.HEP[i]) * int(found.HEP[i])
			# print dotProduct
		return dotProduct

class Circuit:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]
		self.team = []
	
	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2])

# Methods
def parseHEP(line, char):
	return line[line.index(char) + 2:line.find(' ', line.index(char) + 2)]

def match(circuits, name):
	for c in circuits:
		if c.name == name:
			return c

def assignCircuits(jugglers, circuits, cap):
	print "Assigning circuits..."
	i = 0
	"""
	for c in reversed(circuits):
		# print c
		while i < cap:
			for j in jugglers:
				for pref in j.preferences:
					if pref == c.name:
						c.team.append(j)
						jugglers.remove(j)
						i += 1
		# c.team.sort(key=lambda kv: iter(kv.scores).next(), reverse=True)
		i = 0
	"""
	for j in jugglers:
		for p in j.preferences:
			print p
			if len(c.team) < cap:
				c.team.append(j)
				jugglers.remove(j)
			else:
				for team_member in c.team:
					if team_member.score[c] 

def outputFile(circuits):
	fs = open('teams.txt', 'w')
	for c in reversed(circuits):
		fs.write(c.name + ' ')
		for j in c.team:
			fs.write(j.name + ' ')
			# print j.scores
			for key, value in j.scores.items():
				# print key, value
				fs.write(key + ':' + str(value) + ' ')
		fs.write('\n')

def main():
	script, filename = argv
	fs = open(filename)
	jugglers, circuits = [], []

	# builds the lists of jugglers and circuits
	for line in fs:
		# construct circuits
		if line[0] == 'C':
			name = 'C' + line[3:line.find(' ', 3)]
			H = parseHEP(line, 'H')
			E = parseHEP(line, 'E')
			P = parseHEP(line, 'P')
			lastCircuit = Circuit(H, E, P, name)
			circuits.append(lastCircuit)

		# construct jugglers
		elif line[0] == 'J':
			name = 'J' + line[3:line.find(' ', 3)]
			H = parseHEP(line, 'H')
			E = parseHEP(line, 'E')
			P = parseHEP(line, 'P')
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
			scores = dict(zip(split_circuits, dots))
			
			# sorts the new dict in descending order based on value
			scores = OrderedDict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))

			lastJuggler.addLists(split_circuits, scores)
			jugglers.append(lastJuggler)
			# print lastJuggler 

	# now the real fun begins...
	cap = len(jugglers) / len(circuits)
	
	# sort jugglers based on decreasing order of circuit score
	# jugglers.sort(key=lambda kv: iter(kv.scores).next(), reverse=True)
	print '---'
	
	assignCircuits(jugglers, circuits, cap)
	outputFile(circuits)
	
main()
