import sys, os
import copy

def saveAllFace(rubiks):
	save = {'left': copy.deepcopy(rubiks['left']), 'up': copy.deepcopy(rubiks['up']), 'right': copy.deepcopy(rubiks['right']), 'down': copy.deepcopy(rubiks['down']), 'front': copy.deepcopy(rubiks['front']), 'back': copy.deepcopy(rubiks['back'])}
	return save

def rotateFace(rubiksFace, rubiksSave, move):
	if '\'' in move:
		move = 'prime'
	elif '2' in move:
		move = 'double'
	else:
		move = 'simple'

	for i in range(3):
		rubiksFace[0][i] = rubiksSave[2 - i][0] if move == 'simple' else rubiksSave[i][2] if move == 'prime' else rubiksSave[2][2 - i]
		rubiksFace[i][0] = rubiksSave[2][i] if move == 'simple' else rubiksSave[0][2 - i] if move == 'prime' else rubiksSave[2 - i][2]
		rubiksFace[i][2] = rubiksSave[0][i] if move == 'simple' else rubiksSave[2][2 - i] if move == 'prime' else rubiksSave[2 - i][0]
		rubiksFace[2][i] = rubiksSave[2 - i][2] if move == 'simple' else rubiksSave[i][0] if move == 'prime' else rubiksSave[0][2 - i]

def swapbackAndfront(rubiks, move):
	save = saveAllFace(rubiks)
	if move == 'F' or move == 'F\'' or move == 'F2':
		for i in range(3):
			rubiks['left'][i][2] = save['down'][0][i] if move == 'F' else save['up'][2][2 - i] if move == 'F\'' else save['right'][2 - i][0]
			rubiks['up'][2][i] = save['left'][2 - i][2]	if move == 'F' else save['right'][i][0] if move == 'F\'' else save['down'][0][2 - i]
			rubiks['right'][i][0] = save['up'][2][i] if move == 'F' else save['down'][0][2 - i] if move == 'F\'' else save['left'][2 - i][2]
			rubiks['down'][0][i] = save['right'][2 - i][0] if move == 'F' else save['left'][i][2] if move == 'F\'' else save['up'][2][2 - i]
		for i in range(3):
			rotateFace(rubiks['front'], save['front'], move)
	if move == 'B' or move == 'B\'' or move == 'B2':
		for i in range(3):
			rubiks['left'][i][0] = save['up'][0][2 - i] if move == 'B' else save['down'][2][i] if move == 'B\'' else save['right'][2 - i][2]
			rubiks['up'][0][i] = save['right'][i][2] if move == 'B' else save['left'][2 - i][0] if move == 'B\'' else save['down'][2][2 - i]
			rubiks['right'][i][2] = save['down'][2][2 - i] if move == 'B' else save['up'][0][i] if move == 'B\'' else save['left'][2 - i][0]
			rubiks['down'][2][i] = save['left'][i][0] if move == 'B' else save['right'][2 - i][2] if move == 'B\'' else save['up'][0][2 - i]
		for i in range(3):
			rotateFace(rubiks['back'], save['back'], move)

def swapupAnddown(rubiks, move):
	save = saveAllFace(rubiks)
	if move == 'U' or move == 'U\'' or move == 'U2':
		rubiks['left'][0] = save['front'][0] if move == 'U' else save['back'][0] if move == 'U\'' else save['right'][0]
		rubiks['back'][0] = save['left'][0]	if move == 'U' else save['right'][0] if move == 'U\'' else save['front'][0]
		rubiks['right'][0] = save['back'][0] if move == 'U' else save['front'][0] if move == 'U\'' else save['left'][0]
		rubiks['front'][0] = save['right'][0] if move == 'U' else save['left'][0] if move == 'U\'' else save['back'][0]
		for i in range(3):
			rotateFace(rubiks['up'], save['up'], move)
	if move == 'D' or move == 'D\'' or move == 'D2':
		rubiks['left'][2] = save['back'][2] if move == 'D' else save['front'][2] if move == 'D\'' else save['right'][2]
		rubiks['back'][2] = save['right'][2]	if move == 'D' else save['left'][2] if move == 'D\'' else save['front'][2]
		rubiks['right'][2] = save['front'][2] if move == 'D' else save['back'][2] if move == 'D\'' else save['left'][2]
		rubiks['front'][2] = save['left'][2] if move == 'D' else save['right'][2] if move == 'D\'' else save['back'][2]
		for i in range(3):
			rotateFace(rubiks['down'], save['down'], move)

def swaprightAndleft(rubiks, move):
	save = saveAllFace(rubiks)
	if move == 'R' or move == 'R\'' or move == 'R2':
		for i in range(3):
			rubiks['up'][i][2] = save['front'][i][2] if move == 'R' else save['back'][2 - i][0] if move == 'R\'' else save['down'][i][2]
			rubiks['back'][i][0] = save['up'][2 - i][2]	if move == 'R' else save['down'][2 - i][2] if move == 'R\'' else save['front'][2 - i][2]
			rubiks['down'][i][2] = save['back'][2 - i][0] if move == 'R' else save['front'][i][2] if move == 'R\'' else save['up'][i][2]
			rubiks['front'][i][2] = save['down'][i][2] if move == 'R' else save['up'][i][2] if move == 'R\'' else save['back'][2 - i][0]
		for i in range(3):
			rotateFace(rubiks['right'], save['right'], move)
	if move == 'L' or move == 'L\'' or move == 'L2':
		for i in range(3):
			rubiks['up'][i][0] = save['back'][2 - i][2] if move == 'L' else save['front'][i][0] if move == 'L\'' else save['down'][i][0]
			rubiks['back'][i][2] = save['down'][2 - i][0]	if move == 'L' else save['up'][2 - i][0] if move == 'L\'' else save['front'][2 - i][0]
			rubiks['down'][i][0] = save['front'][i][0] if move == 'L' else save['back'][2 - i][2] if move == 'L\'' else save['up'][i][0]
			rubiks['front'][i][0] = save['up'][i][0] if move == 'L' else save['down'][i][0] if move == 'L\'' else save['back'][2 - i][2]
		for i in range(3):
			rotateFace(rubiks['left'], save['left'], move)

def allCmdMove(move, rubiks):
	if move == 'R' or move == 'R\'' or move == 'R2' or move == 'L' or move == 'L\'' or move == 'L2':
		swaprightAndleft(rubiks, move)
	elif move == 'F'  or move == 'F\'' or move == 'F2' or move == 'B' or move == 'B\'' or move == 'B2':
		swapbackAndfront(rubiks, move)
	elif move == 'U' or move == 'U\'' or move == 'U2' or move == 'D' or move == 'D\'' or move == 'D2':
		swapupAnddown(rubiks, move)
	return rubiks