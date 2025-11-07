player_x = 0
player_y = 0

treasure_x = 5
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (up/down/left/right): ")

print(f"Player position: ({player_x}, {player_y})")
while game_running:
    move = input("Enter move (up/down/left/right)"):

    if move == "right":
        player_x += 1
    if move == "left":
        player_x += 1
    if move == "up":
        player_x += 1
    if move == "down":
        player_x += 1

print(f"Score - You: {player_score}, Computer: {computer_score}\n")

if player_score == 2:
    print("You won the game!")
else:
    print("Computer won the game!")
