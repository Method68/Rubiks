from swapBlock import *

def findFinalCornerPos(finalRubiks):
	finalcornerpos = []
	for elem in finalRubiks:
		i = 0
		if elem != 'down' and elem != 'up':
			for row in finalRubiks[elem]:
				j = 0
				if i == 0:
					for value in row:
						if j == 0 or j == 2:
							finalcornerpos.append((elem, i, j, value))
						j += 1
				i += 1
		if elem == 'up':
			for row in finalRubiks[elem]:
					j = 0
					if i == 0 or i == 2:
						for value in row:
							if j == 0 or j == 2:
								finalcornerpos.append((elem, i, j, value))
							j += 1
					i += 1
	
	return finalcornerpos

def firstMove(rubiks, allmovetoresolverubiks):
	totalmove = "B U B' U B U2 B' U2 B' U' B U' B' U2 B U2"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def secondMove(rubiks, allmovetoresolverubiks):
	totalmove = "L U L' U L U2 L' U2 L' U' L U' L' U2 L U2"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def thirdMove(rubiks, allmovetoresolverubiks):
	totalmove = "R U R' U R U2 R' U2 R' U' R U' R' U2 R U2"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def fourMove(rubiks, allmovetoresolverubiks):
	totalmove = "F U F' U F U2 F' U2 F' U' F U' F' U2 F U2"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def resolveFinalFace(rubiks, finalRubiks, allmovetoresolverubiks):
	allcornerinpos = False
	finalcornerpos = findFinalCornerPos(finalRubiks)
	while allcornerinpos == False:
		upZeroZero = False
		upZeroTwo = False
		upTwoZero = False
		upTwoTwo = False
		currentcornerpos = findFinalCornerPos(rubiks)
		for elem in currentcornerpos:
			for elem1 in finalcornerpos:
				if elem[0] == 'up' and elem[1] == 0 and elem[2] == 0:
					if elem1[0] == 'up' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upZeroZero = True
				elif elem[0] == 'up' and elem[1] == 0 and elem[2] == 2:
					if elem1[0] == 'up' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upZeroTwo = True
				elif elem[0] == 'up' and elem[1] == 2 and elem[2] == 0:
					if elem1[0] == 'up' and elem1[1] == 2 and elem1[2] == 0 and elem[3] == elem1[3]:
						upTwoZero = True
				elif elem[0] == 'up' and elem[1] == 2 and elem[2] == 2:
					if elem1[0] == 'up' and elem1[1] == 2 and elem1[2] == 2 and elem[3] == elem1[3]:
						upTwoTwo = True
						
		if upZeroZero == True and upZeroTwo == True and upTwoZero == True and upTwoTwo == True:
			allcornerinpos = True
		elif upZeroZero == True and upZeroTwo == True:
			firstMove(rubiks, allmovetoresolverubiks)
		elif upZeroZero == True and upTwoZero == True:
			secondMove(rubiks, allmovetoresolverubiks)
		elif upZeroTwo == True and upTwoTwo == True:
			thirdMove(rubiks, allmovetoresolverubiks)
		elif upTwoZero == True and upTwoTwo == True:
			fourMove(rubiks, allmovetoresolverubiks)
		elif upZeroZero == True and upZeroTwo == False:
			firstMove(rubiks, allmovetoresolverubiks)
		elif upZeroZero == False and upTwoZero == True:
			secondMove(rubiks, allmovetoresolverubiks)
		elif upZeroTwo == True and upTwoTwo == False:
			thirdMove(rubiks, allmovetoresolverubiks)
		elif upTwoZero == False and upTwoTwo == True:
			fourMove(rubiks, allmovetoresolverubiks)
		else:
			firstMove(rubiks, allmovetoresolverubiks)
