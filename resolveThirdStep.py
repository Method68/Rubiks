from swapBlock import *

def findUpPos(rubiks, valuecross):
	allupvalue = []
	i = 0
	pos = 0
	for elem in rubiks:
		if elem == 'up':
			for row in rubiks[elem]:
				for value in row:
					if value in valuecross:
						pos = row.index(value)
						allupvalue.append((i, pos, value))
				i += 1
	allupvalue.sort()
	return allupvalue

def valueCross(finalRubiks):
	i = 0
	valuecross = []
	for elem in finalRubiks:
		if elem == 'up':
			for row in finalRubiks[elem]:
				j = 0
				for value in row:
					if i == 0 or i == 2:
						if j == 1:
							valuecross.append(value)
					if i == 1:
						valuecross.append(value)
					j += 1
				i += 1
	valuecross.sort()			
	return valuecross

def moveUp(rubiks, allmovetoresolverubiks):
	totalmove = "U"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def createCross(rubiks, allmovetoresolverubiks):
	totalmove = "R' U' F' U F R"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def resolveThirdCross(rubiks, finalRubiks, allmovetoresolverubiks):
	valuecross = valueCross(finalRubiks)
	finduppos = findUpPos(rubiks, valuecross)
	i = 0
	while 1:
		finduppos = findUpPos(rubiks, valuecross)
		if len(finduppos) >= 3:
			for elem in finduppos:
				if len(finduppos) == 5:
					return
				if i == 3:
					createCross(rubiks, allmovetoresolverubiks)
					i = 0
					break
				if elem[0] == 0 and elem[1] == 1:
					for elem in finduppos:
						if elem[0] == 1 and elem[1] == 0:
							createCross(rubiks, allmovetoresolverubiks)
							return
				else:
					moveUp(rubiks, allmovetoresolverubiks)
					i += 1
		else:
			createCross(rubiks, allmovetoresolverubiks)