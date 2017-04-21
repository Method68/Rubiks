from resolveSecondFace import *
from swapBlock import *

def allRingPos(rubiks, allringvalue):
	allringpos = []
	for value in allringvalue:
		for elem in rubiks:
			i = 0
			for row in rubiks[elem]:
				if value[0] in row:
					pos = row.index(value[0])
					if value[1] != elem:
						allringpos.append((elem, i, pos, value[1], value[2], value[3]))
					elif value[2] != i or value[3] != pos:
						allringpos.append((elem, i, pos, value[1], value[2], value[3]))
				i += 1
	return allringpos

def allRingValue(finalRubiks):
	allringvalue = []
	for elem in finalRubiks:
		i = 0
		if elem != 'down' and elem != 'up':
			for row in finalRubiks[elem]:
				if i == 1:
					allringvalue.append((row[0], elem, i, 0))
					allringvalue.append((row[2], elem, i, 2))
				i += 1
	return allringvalue

def resolveRing(rubiks, finalRubiks, allringvalue, allmovetoresolverubiks):
	while 1:
		allringpos = allRingPos(rubiks, allringvalue)
		if allringpos == []:
			break
		move = allMoveForRing(allringpos[0])
		totalmove = move[str(allringpos[0][1])][str(allringpos[0][2])][str(allringpos[0][3])][str(allringpos[0][4])][str(allringpos[0][5])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)

def resolveSecondRing(rubiks, finalRubiks, allmovetoresolverubiks):
	allringvalue = allRingValue(finalRubiks)
	resolveRing(rubiks, finalRubiks, allringvalue, allmovetoresolverubiks)