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

def firstUp(rubiks, allmovetoresolverubiks):
	totalmove = "L R' U L' U' R U L U' L'"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def secondUp(rubiks, allmovetoresolverubiks):
	totalmove = "B F' U B' U' F U B U' B'"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def thirdUp(rubiks, allmovetoresolverubiks):
	totalmove = "F B' U F' U' B U F U' F'"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def fourUp(rubiks, allmovetoresolverubiks):
	totalmove = "R L' U R' U' L U R U' R'"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)
def noUp(rubiks, allmovetoresolverubiks):
	totalmove = "L R' U L' U' R U L U' L'"
	allmovetoresolverubiks.append(totalmove)
	totalmove = totalmove.split(" ")
	for move in totalmove:
		rubiks = allCmdMove(move, rubiks)

def resolveFiveCorner(rubiks, finalRubiks, allmovetoresolverubiks):
	allcornerinpos = False
	while allcornerinpos == False:
		i = 0
		upZeroZero = False
		upZeroTwo = False
		upTwoZero = False
		upTwoTwo = False
		finalcornerpos = findFinalCornerPos(finalRubiks)
		currentcornerpos = findFinalCornerPos(rubiks)
		for elem in currentcornerpos:
			for elem1 in finalcornerpos:
				if elem[0] == 'up' and elem[1] == 0 and elem[2] == 0:
					if elem1[0] == 'up' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upZeroZero = True
					elif elem1[0] == 'back' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upZeroZero = True
					elif elem1[0] == 'left' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upZeroZero = True
				elif elem[0] == 'up' and elem[1] == 0 and elem[2] == 2:
					if elem1[0] == 'up' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upZeroTwo = True
					elif elem1[0] == 'back' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upZeroTwo = True
					elif elem1[0] == 'right' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upZeroTwo = True
				elif elem[0] == 'up' and elem[1] == 2 and elem[2] == 0:
					if elem1[0] == 'up' and elem1[1] == 2 and elem1[2] == 0 and elem[3] == elem1[3]:
						upTwoZero = True
					elif elem1[0] == 'front' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upTwoZero = True
					elif elem1[0] == 'left' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upTwoZero = True
				elif elem[0] == 'up' and elem[1] == 2 and elem[2] == 2:
					if elem1[0] == 'up' and elem1[1] == 2 and elem1[2] == 2 and elem[3] == elem1[3]:
						upTwoTwo = True
					elif elem1[0] == 'front' and elem1[1] == 0 and elem1[2] == 2 and elem[3] == elem1[3]:
						upTwoTwo = True
					elif elem1[0] == 'right' and elem1[1] == 0 and elem1[2] == 0 and elem[3] == elem1[3]:
						upTwoTwo = True
		
		if upZeroZero == True and upZeroTwo == False and upTwoZero == False and upTwoTwo == False:
			firstUp(rubiks, allmovetoresolverubiks)
		elif upZeroZero == False and upZeroTwo == True and upTwoZero == False and upTwoTwo == False:
			secondUp(rubiks, allmovetoresolverubiks)
		elif upZeroZero == False and upZeroTwo == False and upTwoZero == True and upTwoTwo == False:
			thirdUp(rubiks, allmovetoresolverubiks)
		elif upZeroZero == False and upZeroTwo == False and upTwoZero == False and upTwoTwo == True:
			fourUp(rubiks, allmovetoresolverubiks)
		elif upZeroZero == False and upZeroTwo == False and upTwoZero == False and upTwoTwo == False:
			noUp(rubiks, allmovetoresolverubiks)
		else:
			allcornerinpos = True