def elem0(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': 'L2', '1': '', '2': 'U\' L2'}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'U L2', '1': '', '2': 'F2'}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': 'L\' U2 L', '1': '', '2': 'B\' L\' U2 L'}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'B L\' U2 L', '1': '' , '2': 'L\''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': 'U\' L', '1': '', '2': 'F\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'L U L2 U2 L', '1': '', '2': 'L\' U2 L F U2 F\''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': 'L\' U L', '1': '', '2': 'F U2 F\''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'F', '1': '', '2': 'R2 L\' U L'}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': 'L', '1': '', '2': 'F\' L'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'F L', '1': '', '2': 'F2 L'}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': 'D\''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'D', '1': '', '2': 'D2'}}
		return allUpMove
def elem1(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': '', '1': 'U R2 L\' D\' L', '2': ''}, '1': {'0': 'U2 R2 L\' D\' L', '1': '','2': 'R2 L\' D\' L'}, '2': {'0': '', '1': 'U\' R2 L\' D\' L', '2': ''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': '', '1': 'B\' R L\' D\' L', '2': ''}, '1': {'0': 'R L\' D\' L', '1': '','2': 'B2 R L\' D\' L'}, '2': {'0': '', '1': 'B R L\' D\' L' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': '', '1': 'U B\' R L\' D\' L', '2': ''}, '1': {'0': 'L U L\' B\' R L\' D\' L', '1': '','2': 'F\' R U L'}, '2': {'0': '', '1': 'F D\' F\' B R L\' D\' L', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': '', '1': 'U\' B\' R L\' D\' L', '2': ''}, '1': {'0': 'R U\' B\' R L\' D\' L', '1': '', '2': 'R\' U\' B\' R L\' D\' L'}, '2': {'0': '', '1': 'R2 U\' B\' R L\' D\' L', '2': ''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': '', '1': 'U2 B\' R L\' D\' L', '2': ''}, '1': {'0': 'D2 L\' D2 U2 R2 L\' D\' L', '1': '','2': 'R\' L\' D\' L'}, '2': {'0': '', '1': 'L\' D L R2 U\' B\' R L\' D\' L', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': 'F D U F U\' F\'', '1': '', '2': 'L\' D\' L'}, '2': {'0': '', '1': 'L\' D2 L', '2': ''}}
		return allUpMove
def elem2(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': 'U R2', '1': '', '2': 'R2'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'U2 R2', '1': '', '2': 'U\' R2'}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': 'R\' U\' R2', '1': '', '2': 'B\' R\' U\' R2'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'R', '1': '' , '2': 'B R'}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': 'U R\' U\' R2', '1': '', '2': 'U B\' R\' U\' R2'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'F\' L U F R\' U\' R2', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': 'U\' R\' U\' R2', '1': '', '2': 'B U R2'}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'R U\' R\' U\' R2', '1': '', '2': 'R\' B U R2'}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': 'U2  R\' U\' R2', '1': '', '2': 'R\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': 'R U\' R2'}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': 'B R\' B U R2', '1': '', '2': 'B2 U R2'}}
		return allUpMove
def elem3(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': '', '1': 'B2 F2 D F2', '2': ''}, '1': {'0': 'U B2 F2 D F2', '1': '','2': 'U\' B2 F2 D F2'}, '2': {'0': '', '1': 'U2 B2 F2 D F2', '2': ''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': '', '1': 'B F\' L\' F', '2': ''}, '1': {'0': 'B2 F\' L\' F', '1': '','2': 'F\' L\' F'}, '2': {'0': '', '1': 'B\' F\' L\' F' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': '', '1': 'U B F\' L\' F', '2': ''}, '1': {'0': 'D L D\' U B F\' L\' F', '1': '','2': 'D L\' D\' U B F\' L\' F'}, '2': {'0': '', '1': 'F\' L2 F U B F\' L\' F', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': '', '1': 'U\' B F\' L\' F', '2': ''}, '1': {'0': 'D\' R D U\' B F\' L\' F', '1': '', '2': 'D\' R\' D U\' B F\' L\' F'}, '2': {'0': '', '1': 'F R2 F\' U\' B F\' L\' F', '2': ''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': '', '1': 'U2 B F\' L\' F', '2': ''}, '1': {'0': 'D2 F D2 U2 B F\' L\' F', '1': '','2': 'D2 F\' D2 U2 B F\' L\' F'}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': 'F2 D2 F2'}, '2': {'0': '', '1': 'F2 D F2', '2': ''}}
		return allUpMove
def elem4(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
def elem5(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': '', '1': 'U F R2 F\'', '2': ''}, '1': {'0': 'U2 F R2 F\'', '1': '', '2': 'F R2 F\''}, '2': {'0': '', '1': 'U\' F R2 F\'', '2': ''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': '', '1': 'B\' F R F\'', '2': ''}, '1': {'0': 'F R F\'', '1': '','2': 'B2 F R F\''}, '2': {'0': '', '1': 'B F R F\'' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': '', '1': 'U B\' F R F\'', '2': ''}, '1': {'0': 'D L D\' U B\' F R F\'', '1': '','2': 'D L\' D\' U B\' F R F\''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': '', '1': 'U\' B\' F R F\'', '2': ''}, '1': {'0': 'D\' R D U\' B\' F R F\'', '1': '', '2': 'D\' R\' D U\' B\' F R F\''}, '2': {'0': '', '1': 'R U R2 B U\' R\' U2 F R2 F\'', '2': ''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': '', '1': 'U2 B\' F R F\'', '2': ''}, '1': {'0': 'D2 F D2 U2 B\' F R F\'', '1': '','2': 'D2 F\' D2 U2 B\' F R F\''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': 'B2 U F R2 F\'', '2': ''}}
		return allUpMove
def elem6(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': 'U B2', '1': '', '2': 'B2'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'U2 B2', '1': '', '2': 'U\' B2'}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': 'R\' U R U2 B2', '1': '', '2': 'B\' U\' B'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'B R\' U R U2 B2', '1': '' , '2': 'B2 R\' U R U2 B2'}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': 'B', '1': '', '2': 'U B\' U\' B'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'B\' U B2', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': 'U\' R\' U R U2 B2', '1': '', '2': 'L U\' L\'' }, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': 'B\''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': 'U B', '1': '', '2': 'U2 B\' U\' B'}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': 'B2 U B2'}}
		return allUpMove
def elem7(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': '', '1': 'B2 U\' L U2 L\' U2 B\' U B', '2': ''}, '1': {'0': 'U B2 U\' L U2 L\' U2 B\' U B', '1': '', '2': 'U\' B2 U\' L U2 L\' U2 B\' U B'}, '2': {'0': '', '1': 'U2 B2 U\' L U2 L\' U2 B\' U B', '2': ''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': '', '1': 'B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '2': ''}, '1': {'0': 'B\' U\' B D\' R D B\' U B', '1': '','2': 'B2 U2 D\' R D U B\' U B L U2 L\''}, '2': {'0': '', '1': 'B2 U\' B U B\' D\' R D B\' U B L U2 L\'' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': '', '1': 'U B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '2': ''}, '1': {'0': 'D L U L\' D\' B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '1': '','2': 'B2 D L\' D\' B2 U B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B'}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': '', '1': 'U\' B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '2': ''}, '1': {'0': 'D\' R U\' R\' D B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '1': '', '2': 'B U\' B\' U B2 U\' L U2 L\' U2 B\' U B'}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': '', '1': 'U2 B\' D\' R\' D B U\' B2 U\' L U2 L\' U2 B\' U B', '2': ''}, '1': {'0': 'D L\' U L U F U\' F\' D\' B2 U\' L U2 L\' U2 B\' U B', '1': '','2': 'D\' R\' D U2 B\' U B'}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
def elem8(elemCase):
	if elemCase[0] == 'up':
		allUpMove = {'0': {'0': 'U R\' U R B U2 B\'', '1': '', '2': 'R\' U R B U2 B\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'U2 R\' U R B U2 B\'', '1': '', '2': 'U\' R\' U R B U2 B\''}}
		return allUpMove
	if elemCase[0] == 'back':
		allUpMove = {'0': {'0': 'R\' U R U2 R\' U R B U2 B\'', '1': '', '2': 'B\' D\' R\' D B U\' R\' U R B U2 B\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': 'R\' U\' R U R\' U R B U2 B\'', '1': '' , '2': ''}}
		return allUpMove
	if elemCase[0] == 'left':
		allUpMove = {'0': {'0': 'U R\' U R U2 R\' U R B U2 B\'', '1': '', '2': 'U B\' D\' R\' D B U\' R\' U R B U2 B\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'right':
		allUpMove = {'0': {'0': 'U\' R\' U R U2 R\' U R B U2 B\'', '1': '', '2': 'U\' B\' D\' R\' D B U\' R\' U R B U2 B\''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': 'B U B\' U\' R\' U R B U2 B\''}}
		return allUpMove
	if elemCase[0] == 'front':
		allUpMove = {'0': {'0': 'U2 R\' U R U2 R\' U R B U2 B\'', '1': '', '2': 'U2 B\' D\' R\' D B U\' R\' U R B U2 B\''}, '1': {'0': '', '1': '','2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove
	if elemCase[0] == 'down':
		allUpMove = {'0': {'0': '', '1': '', '2': ''}, '1': {'0': '', '1': '', '2': ''}, '2': {'0': '', '1': '', '2': ''}}
		return allUpMove