# Yodle Jugglefest Challenge
# author @Patrick Wu

import sys, numpy
from Juggler import Juggler
from Circuit import Circuit
from collections import OrderedDict


def main():
	fs = open('juggletest.txt')
	jugglers, circuits = [], []

	# builds the lists of jugglers and circuits
	for line in fs:
		# construct circuits
		if line[0] == 'C':
			name = 'C' + line[3:line.find(' ', 3)]
			H = line[line.index('H') + 2]
			E = line[line.index('E') + 2]
			P = line[line.index('P') + 2]
			lastCircuit = Circuit(H, E, P, name)
			circuits.append(lastCircuit)
			print lastCircuit

		# construct jugglers
		elif line[0] == 'J':
			name = 'J' + line[3:line.find(' ', 3)]
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
			print dots

			# zips these two lists into a dict
			preferences = dict(zip(split_circuits, dots))
			
			# sorts the new dict in descending order based on value
			d_preferences = OrderedDict(sorted(preferences.items(), key=lambda kv: kv[1], reverse=True))

			lastJuggler.addPreferences(d_preferences)
			jugglers.append(lastJuggler)
			print lastJuggler 

	# now the real fun begins
	# loop through circuits to find the max
	# using binary search
		

main()
