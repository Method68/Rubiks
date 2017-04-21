import sys, os
import copy
from termcolor import colored
from swapBlock import *
from resolveFirstStep import *
from resolveSecondStep import *
from resolveThirdStep import *
from resolveFourStep import *
from resolveFiveStep import *
from resolveFinalStep import *

def createRubiks():
	red = '\033[0;30;41m'
	yellow = '\033[0;30;43m'
	green = '\033[0;30;42m'
	blue = '\033[0;37;44m'
	black = '\033[0;37;48m'
	orange = '\033[0;37;45m'
	white = '\033[0m'
	up     = [[red+'R1'+white, red+'R2'+white, red+'R3'+white], [red+'R4'+white, red+'R5'+white, red+'R6'+white], [red+'R7'+white, red+'R8'+white, red+'R9'+white]]
	front  = [[yellow+'Y1'+white,yellow+'Y2'+white,yellow+'Y3'+white], [yellow+'Y4'+white,yellow+'Y5'+white,yellow+'Y6'+white], [yellow+'Y7'+white,yellow+'Y8'+white,yellow+'Y9'+white]]
	left   = [[green+'G1'+white,green+'G2'+white,green+'G3'+white], [green+'G4'+white,green+'G5'+white,green+'G6'+white], [green+'G7'+white,green+'G8'+white,green+'G9'+white]]
	right  = [[blue+'B1'+white,blue+'B2'+white,blue+'B3'+white], [blue+'B4'+white,blue+'B5'+white,blue+'B6'+white], [blue+'B7'+white,blue+'B8'+white,blue+'B9'+white]]
	back   = [[black+'D1'+white,black+'D2'+white,black+'D3'+white], [black+'D4'+white,black+'D5'+white,black+'D6'+white], [black+'D7'+white,black+'D8'+white,black+'D9'+white]]
	down   = [[orange+'O1'+white,orange+'O2'+white,orange+'O3'+white], [orange+'O4'+white,orange+'O5'+white,orange+'O6'+white], [orange+'O7'+white,orange+'O8'+white,orange+'O9'+white]]
	rubiks = {'up': up,  'left': left, 'front': front, 'right': right, 'back': back, 'down': down}
	return rubiks

def display_line(tab1, tab2, tab3, tab4, raw):
		i = 0
		while (i < 3):
			print (tab1[raw][i], end=' ')
			i += 1
		print ('    ', end=' ')
		i = 0
		while (i < 3):
			print (tab2[raw][i], end=' ')
			i += 1
		print ('    ', end=' ')
		i = 0
		while (i < 3):
			print (tab3[raw][i], end=' ')
			i += 1
		print ('    ', end=' ')
		i = 0
		while (i < 3):
			print (tab4[raw][i], end=' ')
			i += 1
		print ('\n')

def solveRubiks(rubiks, finalRubiks, allmovetoresolverubiks):
	resolveRubiksDown(rubiks, finalRubiks, allmovetoresolverubiks)
	resolveSecondRing(rubiks, finalRubiks, allmovetoresolverubiks)
	resolveThirdCross(rubiks, finalRubiks, allmovetoresolverubiks)
	resolveFourFace(rubiks, finalRubiks, allmovetoresolverubiks)
	resolveFiveCorner(rubiks, finalRubiks, allmovetoresolverubiks)
	resolveFinalFace(rubiks, finalRubiks, allmovetoresolverubiks)
	done = 0
	for elem in rubiks:
		block = 0
		count = 0
		if elem == 'up' or elem == 'down':
			for row in rubiks[elem]:
				raw = 0
				for value in row:
					if ((block == 0) and raw == 0):
						print('             ', end=' ')
					print(value, end=' ')
					raw += 1
				if (block < 1 or block > 4):
					print('\n')
			block += 1
		elif (done == 0):
			display_line(rubiks["left"],rubiks["front"],rubiks["right"],rubiks["back"], 0)
			display_line(rubiks["left"],rubiks["front"],rubiks["right"],rubiks["back"], 1)
			display_line(rubiks["left"],rubiks["front"],rubiks["right"],rubiks["back"], 2)
			done = 1


def applyCmdMove(move, rubiks):
	allmovetoresolverubiks = []
	allmove = move.split(' ')
	for move in allmove:
		rubiks = allCmdMove(move, rubiks)
	done = 0
	for elem in rubiks:
		block = 0
		count = 0
		if elem == 'up' or elem == 'down':
			for row in rubiks[elem]:
				raw = 0
				for value in row:
					if ((block == 0) and raw == 0):
						print('             ', end=' ')
					print(value, end=' ')
					raw += 1
				if (block < 1 or block > 4):
					print('\n')
			block += 1
		elif (done == 0):
			display_line(rubiks["left"],rubiks["right"],rubiks["front"],rubiks["back"], 0)
			display_line(rubiks["left"],rubiks["right"],rubiks["front"],rubiks["back"], 1)
			display_line(rubiks["left"],rubiks["right"],rubiks["front"],rubiks["back"], 2)
			done = 1

	print("\033[91m########################################\n\033[0m")
	finalRubiks = createRubiks()
	solveRubiks(rubiks, finalRubiks, allmovetoresolverubiks)
	i = 0
	for elem in allmovetoresolverubiks:
		if elem != '':
			allelem = elem.split(' ')
			for elem1 in allelem:
				i += 1
			print("\033[92m" + str(elem))
	print("\033[91mTotal move:\033[0m" + str(i))

def main(argv):
	rubiks = createRubiks()
	applyCmdMove(argv, rubiks)

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('\033[91mBad number of argument ! ex: "R L D B F U R2 L2 D2 B2 F2 U2 R\' L\' D\' B\' F\' U\'"')
		exit()
	elif len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print('\033[91mBad number of argument ! ex: "R L D B F U R2 L2 D2 B2 F2 U2 R\' L\' D\' B\' F\' U\'"')
		exit()