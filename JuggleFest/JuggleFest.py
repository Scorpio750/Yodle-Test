import sys, numpy

class Juggler:
	def __init__(self, H, E, P):
		self.HEP = [H, E, P]
	
	def addPreferences(self,preferences):
		self.preferences = preferences[:]
	
class Circuit:
	def __init__(self, H, E, P):
		self.HEP = [H, E, P]
	

def main():
	fs = open('juggletest.txt')
	jugglers, circuits = [], []
	
	# builds the lists of jugglers and circuits
	for line in fs:
		if line[0] == 'C':
			# construct circuits
			H = line[line.index('H') + 2]
			E = line[line.index('E') + 2]
			P = line[line.index('P') + 2]
			lastCircuit = Circuit(H, E, P)
			circuits.append(lastCircuit)	
			print "C" + str(len(circuits)-1) + " H: " + str(lastCircuit.HEP[0]) + " E: " + str(lastCircuit.HEP[1]) + " P: " + str(lastCircuit.HEP[2])
		elif line[0] == 'J':

			# construct jugglers
			H = line[line.index('H') + 2]
			E = line[line.index('E') + 2]
			P = line[line.index('P') + 2]
			lastJuggler = Juggler(H, E, P)
			
			# grabs substring of preferences from substring in original line
			preference_line = line[line.find('C'):]
			split_circuits = preference_line.split(',')
			
			# removes the escapekeys from the last circuit string
			last_split = split_circuits[len(split_circuits)-1]
			split_circuits[len(split_circuits)-1] = last_split.rstrip('\r\n');
			print split_circuits
			lastJuggler.addPreferences(split_circuits)
			jugglers.append(lastJuggler)
			print "J" + str(len(jugglers)-1) + " H: " + str(lastJuggler.HEP[0]) + " E: " + str(lastJuggler.HEP[1]) + " P: " + str(lastJuggler.HEP[2]) + str(lastJuggler.preferences)	
	
	# now the real fun begins
	

main()
