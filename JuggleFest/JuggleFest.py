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
	
	# returns a list of dot products for each circuit
	def dotProduct(self, circuits):
		dotProduct, dotProducts = 0, {}
		# print found
		for c in circuits:
			for i in range(len(self.HEP)):
				dotProduct += int(self.HEP[i]) * int(c.HEP[i])
				dotProducts[c.name] = dotProduct
				# print dotProduct
		
		return dotProducts

class Circuit:
	def __init__(self, H, E, P, name):
		self.name = name
		self.HEP = [H, E, P]
		self.team = []
	
	def __repr__(self):
		return self.name + " H:" + str(self.HEP[0]) + " E:" + str(self.HEP[1]) + " P:" + str(self.HEP[2]) + '\nTeam:: ' + str(len(self.team))

# Methods
def parseHEP(line, char):
	return line[line.index(char) + 2:line.find(' ', line.index(char) + 2)]

def match(circuits, name):
	for c in circuits:
		if c.name == name:
			return c

def assignCircuits(jugglers, circuits, cap):
	print "Assigning circuits..."
	i, assigned_to_pref = 0, False
	
	while len(jugglers) > 0:
		j = jugglers.pop()
		assigned_to_pref = False
		print '\nOn '+ str(j)
		for p in range(len(j.preferences)):
			c = circuits[int(j.preferences[p][1])]
			print 'On preference ' + j.preferences[p]
			print 'On circuit ' + c.name
			if len(c.team) < cap:
				print "Assigning " + j.name + " to " + c.name
				c.team.append(j)
				assigned_to_pref = True
				break
			else:
				print "Cycling through team members"
				for team_member in c.team:
					print team_member
					if p < team_member.preferences.index(j.preferences[p]):
						print j.preferences[p] + ":" + str(p) + " is higher than " + team_member.preferences[team_member.preferences.index(j.preferences[p])] + ":" + str(team_member.preferences.index(j.preferences[p]))
						print "Assigning " + j.name + " to " + c.name
						c.team.append(j)
						print "Removing " + team_member.name + " from " + c.name
						jugglers.append(team_member)
						c.team.remove(team_member)
						assigned_to_pref = True
						break
					elif team_member.scores[c.name] < j.scores[c.name] and p < team_member.preferences.index(j.preferences[p]):
						print "Assigning " + j.name + " to " + c.name
						c.team.append(j)
						print "Removing " + team_member.name + " from " + c.name
						jugglers.append(team_member)
						c.team.remove(team_member)
						assigned_to_pref = True
						break
				if assigned_to_pref:
					break
		# if there isn't room in any of j's preferences, randomly assign him to an unfilled circuit
		if not assigned_to_pref:
			circuits.sort(key=lambda kv: len(kv.team))
			print circuits
			for c in circuits:
				if len(c.team) < cap:
					c.team.append(j)
					print "Assigning " + j.name +  " to " + c.name
					circuits.sort(key=lambda kv: len(kv.team))
					break
				else:
					for team_member in c.team:
						if team_member.scores[c.name] < j.scores[c.name]:
							print "Assigning " + j.name + " to " + c.name
							c.team.append(j)
							print "Removing " + team_member.name + " from " + c.name
							jugglers.append(team_member)
							c.team.remove(team_member)
							break
					break
			circuits.sort(key=lambda kv: int(kv[1]))
			print circuits

def outputFile(circuits):
	fs = open('teams.txt', 'w')
	circuits.sort(key=lambda kv: int(kv.name[1]))
	for c in reversed(circuits):
		fs.write(c.name + ' ')
		for j in c.team:
			fs.write(j.name + ' ')
			# print j.scores
			for p in j.preferences:
				# print key, value
				fs.write(p + ':' + str(j.scores[p]) + ' ')
			fs.seek(-1, 1)
			fs.write(', ')
		fs.seek(-2, 1)
		fs.write('\n')
	fs.truncate()
	fs.close()

def outputResult(circuits):
	fs = open('results.txt', 'r')
	sum_1970 = sum(int(j.name[1]) for j in circuits['C1970'].team)
	fs.write("C1970: " + str(sum_1970))
	fs.close()


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
			# converts list of circuits into dict,
			# where key is the circuit and value is the dot product
			scores = lastJuggler.dotProduct(circuits)

			lastJuggler.addLists(split_circuits, scores)
			jugglers.append(lastJuggler)
			# print lastJuggler 

	# now the real fun begins...
	cap = len(jugglers) / len(circuits)
	
	print '---'
	
	assignCircuits(jugglers, circuits, cap)
	outputFile(circuits)
	if filename == 'jugglefest.txt':
		outputResult(circuits)
	
main()
