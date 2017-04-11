from swapBlock import *

def findElemFinalPos(finalRubiks):
	elemfinalpos = []
	for elem in finalRubiks:
		i = 0
		j = 0
		if elem != 'up' and elem != 'down':
			for row in finalRubiks[elem]:
				if i == 0:
					for value in row:
						if j == 1:
							elemfinalpos.append((elem, i, j, value))
						j += 1
				i += 1
	elemfinalpos.sort()
	return elemfinalpos

def findElemPos(rubiks, elemfinalpos):
	findelempos = []
	for elem in rubiks:
		if elem != 'up' and elem != 'down':
			for row in rubiks[elem]:
				for value in row:
					for elem1 in elemfinalpos:
						if value in elem1:
							findelempos.append((elem, elem1[0]))
	findelempos.sort()
	return findelempos

def moveUp(rubiks, allmovetoresolverubiks):
	totalmove = "U"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def switchPos(rubiks, allmovetoresolverubiks):
	totalmove = "R U R' U R U2 R' U2"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def checkOnlylefTruePos(elempos): 
	i = 0
	for elem in elempos:
		if elem[0] == 'left' and elem[1] == 'left':
			i += 1
		if elem[0] == 'front' and elem[1] == 'front':
			i += 1
		if elem[0] == 'right' and elem[1] == 'right':
			i += 1
		if elem[0] == 'back' and elem[1] == 'back':
			i += 1
	return i

def resolveFourFace(rubiks, finalRubiks, allmovetoresolverubiks):
	elemfinalpos = findElemFinalPos(finalRubiks)
	allpostrue = False
	while allpostrue == False:
		elempos = findElemPos(rubiks, elemfinalpos)
		for elem in elempos:
			if elem[0] == 'left':
				if elem[0] == 'left' and elem[1] == 'left':
					onlylefttruepos = checkOnlylefTruePos(elempos)
					if onlylefttruepos > 1 and onlylefttruepos < 4:
						moveUp(rubiks, allmovetoresolverubiks)
						switchPos(rubiks, allmovetoresolverubiks)
						break
					onlylefttruepos = checkOnlylefTruePos(elempos)
					if onlylefttruepos == 4:
						allpostrue = True
					else:
						allpostrue = False
					if allpostrue == False:
						switchPos(rubiks, allmovetoresolverubiks)
				else:
					moveUp(rubiks, allmovetoresolverubiks)
				break
