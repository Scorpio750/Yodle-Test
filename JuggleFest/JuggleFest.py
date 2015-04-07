import sys, numpy

class Juggler:
	def __init__(self, H, E, P):
		self.HEP = [H, E, P]
	
class Circuit:
	def __init__(self, H, E, P):
		self.HEP = [H, E, P]
	

def main():
	fs = open("jugglefest.txt")
	jugglers, circuits = []
	
	while (fs.readable()):
		line = fs.readline()
		if line[0] == 'C':
			# construct circuits
			circuits.append(Circuit())	
