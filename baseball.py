stealprob = .67 # (Binary)
players = {}
def posit(x):
	if x == -3:
		return "first batter"
	elif x == -2:
		return "second batter"
	elif x == -1:
		return "third batter"
	elif x == 0:
		return "fourth batter"
	elif x == 1:
		return "pitcher"
	elif x == 2:
		return "catcher"
	elif x == 3:
		return "first base"
	elif x == 4:
		return "second base"
	elif x == 5:
		return "third base"
	elif x == 6:
		return "shortstop"
	elif x == 7:
		return "left field"
	elif x == 8:
		return "center field"
	elif x == 9:
		return "right field"
def addplayer(team, num):
	if num == -3:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n"),
			"baseadvanceperc": input("What is the percent chance (do not include the % symbol) that this player makes it from one base to the next?\n"),
			"swingingstrikeperc": input("What is the percent chance (do not include the % symbol) that this player swings on a ball?\n"),
			"hitperc": input("What is the percent chance (do not include the % symbol) that this player gets a hit?\n")
		}
	elif num == -2:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n"),
			"baseadvanceperc": input("What is the percent chance (do not include the % symbol) that this player makes it from one base to the next?\n"),
			"swingingstrikeperc": input("What is the percent chance (do not include the % symbol) that this player swings on a ball?\n"),
			"hitperc": input("What is the percent chance (do not include the % symbol) that this player gets a hit?\n")
		}
	elif num == -1:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n"),
			"baseadvanceperc": input("What is the percent chance (do not include the % symbol) that this player makes it from one base to the next?\n"),
			"swingingstrikeperc": input("What is the percent chance (do not include the % symbol) that this player swings on a ball?\n"),
			"hitperc": input("What is the percent chance (do not include the % symbol) that this player gets a hit?\n")
		}
	elif num == 0:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n"),
			"baseadvanceperc": input("What is the percent chance (do not include the % symbol) that this player makes it from one base to the next?\n"),
			"swingingstrikeperc": input("What is the percent chance (do not include the % symbol) that this player swings on a ball?\n"),
			"hitperc": input("What is the percent chance (do not include the % symbol) that this player gets a hit?\n")
		}
	elif num == 1:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n"),
			"strikeperc": input(f"What is the percent chance (do not include the % symbol) that this player throws a strike whilst pitching?\n")
		}
	elif num == 2:
		pn = "Player "+str(num)
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n")
		}
	elif num >= 3 and num <= 9:
		players[f"{team}{num}"] = {
			"name": input(f"What is the name of the {posit(num)} on {team}?\n")
			}
def start():
	away = input('What is the name of the away team? ("The" will not be added automatically.)\n')
	home = input('What is the name of the home team? ("The" will not be added automatically.)\n')
	count1 = -4
	while count1 < 9:
		count1 += 1
		addplayer(away, count1)
	count1 = -4
	while count1 < 9:
		count1 += 1
		addplayer(home, count1)
		
start()
print(players)