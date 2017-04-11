def allMoveForRing(moveToDest):
	if moveToDest[0] == 'left':
		allMove =	{'0':{'1':
					{'left': {'1': {'0': "U' B' U B U L U' L'", '2': "U F U' F' U' L' U L"}},
					'right': {'1': {'0': "U F' U F U R U' R'", '2': "U' B U' B' U' R' U R"}},
					'front': {'1': {'0': "U2 L' U L U F U' F'", '2': "R U' R' U' F' U F"}},
					'back': {'1': {'0': "R' U R U B U' B'", '2': "U2 L U' L' U' B' U B"}}
					}}, 
		 			'1':{'0':
		 			{'left': {'1': {'0': "", '2': "U' B' U B U L U' L' U' F U' F' U' L' U L"}},
		 			'right': {'1': {'0': "U' B' U B U L U' L' U' F' U F U R U' R'", '2': "U' B' U B U L U' L' U2 R' U R U B U' B'"}},
		 			'front': {'1': {'0': "U' B' U B U L U' L' U' F U' F' U' L' U L", '2': "U' B' U B U L U' L' U' F' U F U R U' R'"}},
		 			'back': {'1': {'0': "U' B' U B U L U' L' U B U' B' U' R' U R", '2': "U' B' U B U L U' L' U B' U B U L U' L'"}}
		 			},
		 			'2':
		 			{'left': {'1': {'0': "U F U' F' U' L' U L2 U' L' U' B' U B", '2': ""}},
		 			'right': {'1': {'0': "U F U' F' U' L' U L U2 R U' R' U' F' U F", '2': "U F U' F' U' L' U L U2 R' U R U B U' B'"}},
		 			'front': {'1': {'0': "U F U' F' U' L' U L U' F U' F' U' L' U L", '2': "U F U' F' U' L' U L U' F' U F U R U' R'"}},
		 			'back': {'1': {'0': "U F U' F' U' L' U L U B U' B' U' R' U R", '2': "U F U' F' U' L' U L U B' U B U L U' L'"}}
		 			}}
		 			}
		return allMove
	if moveToDest[0] == 'front':
		allMove =	{'0':{'1':
					{'left': {'1': {'0': "B' U B U L U' L'", '2': "U2 F U' F' U' L' U L"}},
					'right': {'1': {'0': "U2 F' U F U R U' R'", '2': "B U' B' U' R' U R"}},
					'front': {'1': {'0': "U' L' U L U F U' F'", '2': "U R U' R' U' F' U F"}},
					'back': {'1': {'0': "U R' U R U B U' B'", '2': "U' L U' L' U' B' U B"}}
					}}, 
		 			'1':{'0':
		 			{'left': {'1': {'0': "L' U L U F U' F' U L U' L' U' B' U B", '2': "L' U L U F U' F' U L' U L U F U' F'"}},
		 			'right': {'1': {'0': "L' U L U F U' F' U' R U' R' U' F' U F", '2': "L' U L U F U' F' U' R' U R U B U' B'"}},
		 			'front': {'1': {'0': "", '2': "L' U L U F U' F' U' R U' R' U' F' U F"}},
		 			'back': {'1': {'0': "L' U L U F U' F' U2 B U' B' U' R' U R", '2': "L' U L U F U' F' U2 B' U B U L U' L'"}}
		 			},
		 			'2':
		 			{'left': {'1': {'0': "R U' R' U' F' U F U L U' L' U' B' U B", '2': "R U' R' U' F' U F U L' U L U F U' F'"}},
		 			'right': {'1': {'0': "R U' R' U' F' U F U' R U' R' U' F' U F", '2': "R U' R' U' F' U F U' R' U R U B U' B'"}},
		 			'front': {'1': {'0': "R U' R' U' F' U F2 U' F' U' L' U L", '2': ""}},
		 			'back': {'1': {'0': "R U' R' U' F' U F U2 B U' B' U' R' U R", '2': "R U' R' U' F' U F U2 B' U B U L U' L'"}}
		 			}}
		 			}
		return allMove
	if moveToDest[0] == 'right':
		allMove =	{'0':{'1':
					{'left': {'1': {'0': "U B' U B U L U' L'", '2': "U' F U' F' U' L' U L"}},
					'right': {'1': {'0': "U' F' U F U R U' R'", '2': "U B U' B' U' R' U R"}},
					'front': {'1': {'0': "L' U L U F U' F'", '2': "U2 R U' R' U' F' U F"}},
					'back': {'1': {'0': "U2 R' U R U B U' B'", '2': "L U' L' U' B' U B"}}
					}}, 
		 			'1':{'0':
		 			{'left': {'1': {'0': "F' U F U R U' R' U2 L U' L' U' B' U B", '2': "F' U F U R U' R' U2 L' U L U F U' F'"}},
		 			'right': {'1': {'0': "", '2': "F' U F U R U' R2 U R U B U' B'"}},
		 			'front': {'1': {'0': "F' U F U R U' R' U F U' F' U' L' U L", '2': "F' U F U R U' R' U F' U F U R U' R'"}},
		 			'back': {'1': {'0': "F' U F U R U' R' U' B U' B' U' R' U R", '2': "F' U F U R U' R' U' B' U B U L U' L'"}}
		 			},
		 			'2':
		 			{'left': {'1': {'0': "B U' B' U' R' U R U2 L U' L' U' B' U B", '2': "B U' B' U' R' U R U2 L' U L U F U' F'"}},
		 			'right': {'1': {'0': "B U' B' U' R' U R2 U' R' U' F' U F", '2': ""}},
		 			'front': {'1': {'0': "B U' B' U' R' U R U F U' F' U' L' U L", '2': "B U' B' U' R' U R U F' U F U R U' R'"}},
		 			'back': {'1': {'0': "B U' B' U' R' U R U' B U' B' U' R' U R", '2': "B U' B' U' R' U R U' B' U B U L U' L'"}}
		 			}}
		 			}
		return allMove
	if moveToDest[0] == 'back':
		allMove =	{'0':{'1':
					{'left': {'1': {'0': "U2 B' U B U L U' L'", '2': "F U' F' U' L' U L"}},
					'right': {'1': {'0': "F' U F U R U' R'", '2': "U2 B U' B' U' R' U R"}},
					'front': {'1': {'0': "U L' U L U F U' F'", '2': "U' R U' R' U' F' U F"}},
					'back': {'1': {'0': "U' R' U R U B U' B'", '2': "U L U' L' U' B' U B"}}
					}}, 
		 			'1':{'0':
		 			{'left': {'1': {'0': "R' U R U B U' B' U' L U' L' U' B' U B", '2': "R' U R U B U' B' U' L' U L U F U' F'"}},
		 			'right': {'1': {'0': "R' U R U B U' B' U R U' R' U' F' U F", '2': "R' U R U B U' B' U R' U R U B U' B'"}},
		 			'front': {'1': {'0': "R' U R U B U' B' U2 F U' F' U' L' U L", '2': "R' U R U B U' B' U2 F' U F U R U' R'"}},
		 			'back': {'1': {'0': "", '2': "R' U R U B U' B2 U B U L U' L'"}}
		 			},
		 			'2':
		 			{'left': {'1': {'0': "L U' L' U' B' U B U' L U' L' U' B' U B", '2': "L U' L' U' B' U B U' L' U L U F U' F'"}},
		 			'right': {'1': {'0': "L U' L' U' B' U B U R U' R' U' F' U F", '2': "L U' L' U' B' U B U R' U R U B U' B'"}},
		 			'front': {'1': {'0': "L U' L' U' B' U B U2 F U' F' U' L' U L", '2': "L U' L' U' B' U B U2 F' U F U R U' R'"}},
		 			'back': {'1': {'0': "L U' L' U' B' U B2 U' B' U' R' U R", '2': ""}}
		 			}}
		 			}
		return allMove
	if moveToDest[0] == 'up':
		allMove =	{'0':{'1':
					{'left': {'1': {'0': "U L U' L' U' B' U B", '2': "U L' U L U F U' F'"}},
					'right': {'1': {'0': "U' R U' R' U' F' U F", '2': "U' R' U R U B U' B'"}},
					'front': {'1': {'0': "F U' F' U' L' U L", '2': "F' U F U R U' R'"}},
					'back': {'1': {'0': "U2 B U' B' U' R' U R", '2': "U2 B' U B U L U' L'"}}
					}}, 
		 			'1':{'0':
		 			{'left': {'1': {'0': "U2 L U' L' U' B' U B", '2': "U2 L' U L U F U' F'"}},
		 			'right': {'1': {'0': "R U' R' U' F' U F", '2': "R' U R U B U' B'"}},
		 			'front': {'1': {'0': "U F U' F' U' L' U L", '2': "U F' U F U R U' R'"}},
		 			'back': {'1': {'0': "U' B U' B' U' R' U R", '2': "U' B' U B U L U' L'"}}
		 			},
		 			'2':
		 			{'left': {'1': {'0': "L U' L' U' B' U B", '2': "L' U L U F U' F'"}},
		 			'right': {'1': {'0': "U2 R U' R' U' F' U F", '2': "U2 R' U R U B U' B'"}},
		 			'front': {'1': {'0': "U' F U' F' U' L' U L", '2': "U' F' U F U R U' R'"}},
		 			'back': {'1': {'0': "U B U' B' U' R' U R", '2': "U B' U B U L U' L'"}}
		 			}},
		 			'2': {'1':
					{'left': {'1': {'0': "U R' U R U B U' B'", '2': "U' L' U L U F U' F'"}},
					'right': {'1': {'0': "U R U' R' U' F' U F", '2': "U R' U R U B U' B'"}},
					'front': {'1': {'0': "U2 F U' F' U' L' U L", '2': "U2 F' U F U R U' R'"}},
					'back': {'1': {'0': "B U' B' U' R' U R", '2': "B' U B U L U' L'"}}
					}}
					}
		return allMove