from resolveFirstFace import *
from swapBlock import *
from main import *

def getElem(rubiks, finalRubiks, raw, col):
	allPosDown = (None, None, None)
	value = finalRubiks['down'][raw][col]
	for elem1 in rubiks:
		i = 0
		for row1 in rubiks[elem1]:
			if value in row1:
				pos = row1.index(value)
				allPosDown = (elem1, i, pos)
				return(allPosDown)
			i += 1

def moveCase(elemCase, rubiks, coordinate, numberElem, allmovetoresolverubiks):
	if numberElem == 0:
		move = elem0(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 1:
		move = elem1(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 2:
		move = elem2(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 3:
		move = elem3(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 4:
		move = elem4(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 5:
		move = elem5(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 6:
		move = elem6(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 7:
		move = elem7(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)
	elif numberElem == 8:
		move = elem8(elemCase)
		totalmove = move[str(elemCase[1])][str(elemCase[2])]
		allmovetoresolverubiks.append(totalmove)
		totalmove = totalmove.split(" ")
		for move in totalmove:
			rubiks = allCmdMove(move, rubiks)

def resolveRubiksDown(rubiks, finalRubiks, allmovetoresolverubiks):
	raw = -1
	col = 0
	numberElem = 0
	for elem in range(9):
		if elem % 3 == 0:
			raw += 1
			col = 0		
		pos = getElem(rubiks, finalRubiks, raw, col)
		moveCase(pos, rubiks, finalRubiks, numberElem, allmovetoresolverubiks)
		col += 1
		numberElem += 1
	return rubiks