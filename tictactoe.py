import os

def emptyCheck(screen, x, y):
	if screen[x][y] == '-':
		return True
	else:
		return False
def screenWrite(screen, x, y, OTurn):
	if OTurn == True and emptyCheck(screen, x, y):
		screen[x][y] = 'O'
	elif OTurn == False and emptyCheck(screen, x, y):
		screen[x][y] = 'X'

def winCheck(screen):
	if screen[0][0] == screen[1][1] == screen[2][2] != '-':
		return screen[0][0]
	elif screen[0][2] == screen[1][1] == screen[2][0] != '-':
		return screen[0][2]
	elif screen[0][0] == screen[0][1] == screen[0][2] != '-':
		return screen[0][0]
	elif screen[1][0] == screen[1][1] == screen[1][2] != '-':
		return screen[1][0]
	elif screen[2][0] == screen[2][1] == screen[2][2] != '-':
		return screen[2][0]
	elif screen[0][0] == screen[1][0] == screen[2][0] != '-':
		return screen[0][0]
	elif screen[0][1] == screen[1][1] == screen[2][1] != '-':
		return screen[0][1]
	elif screen[0][2] == screen[1][2] == screen[2][2] != '-':
		return screen[0][2]
	else:
		return False

def render(screen):
	for i in range(3):
		for j in range(3):
			print(f'{screen[i][j]} ', end='')
		print()


GameOver = False
count = 0
OTurn = True
screen = [['-', '-', '-'], ['-', '-', '-'],['-', '-', '-']]

while GameOver == False :
	rightAns = False
	render(screen)
	while rightAns == False:
		if OTurn == True:
			ans = input("O의 차례입니다. 놓을 곳(X Y)을 입력하세요: ")
			x = int(ans.split(' ')[0])
			y = int(ans.split(' ')[1])
			if x < 0 or x > 2 or y < 0 or y >2 or emptyCheck(screen, x, y) != True:
				print(f"잘못된 입력입니다.")
			else:
				rightAns = True
		else:
			ans = input("X의 차례입니다. 놓을 곳(X Y)을 입력하세요: ")
			x = int(ans.split(' ')[0])
			y = int(ans.split(' ')[1])
			if x < 0 or x > 2 or y < 0 or y >2 or emptyCheck(screen, x, y) != True:
				print("잘못된 입력입니다.")
			else:
				rightAns = True
	
	os.system('clear')
	screenWrite(screen, x, y, OTurn)
	count += 1
	
	OTurn = not OTurn

	if winCheck(screen) != False:
		print(f'{winCheck(screen)}이 승리했습니다!')
		GameOver = True

	if count == 9 and GameOver == False:
		print(f'무승부 입니다.')
		GameOver = True
