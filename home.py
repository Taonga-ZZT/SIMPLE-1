import random
import os

WIDTH = 15
HEIGHT = 10

# Create map
dungeon = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Add walls
for x in range(WIDTH):
    dungeon[0][x] = "#"
    dungeon[HEIGHT - 1][x] = "#"

for y in range(HEIGHT):
    dungeon[y][0] = "#"
    dungeon[y][WIDTH - 1] = "#"

# Random walls
for _ in range(20):
    x = random.randint(1, WIDTH - 2)
    y = random.randint(1, HEIGHT - 2)
    dungeon[y][x] = "#"

player = [1, 1]
treasure = [WIDTH - 2, HEIGHT - 2]
monster = [random.randint(2, WIDTH - 3), random.randint(2, HEIGHT - 3)]

dungeon[treasure[1]][treasure[0]] = "$"

health = 5
gold = 0


def draw():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== ASCII DUNGEON ===")
    print(f"❤️ Health: {health}   💰 Gold: {gold}")
    print("Move: W A S D   |   Q = Quit\n")

    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if [x, y] == player:
                row += "@"
            elif [x, y] == monster:
                row += "M"
            else:
                row += dungeon[y][x]
        print(row)


while True:
    draw()

    move = input("\nYour move: ").lower()

    if move == "q":
        print("You escaped the dungeon!")
        break

    dx, dy = 0, 0

    if move == "w":
        dy = -1
    elif move == "s":
        dy = 1
    elif move == "a":
        dx = -1
    elif move == "d":
        dx = 1
    else:
        continue

    nx = player[0] + dx
    ny = player[1] + dy

    if dungeon[ny][nx] != "#":
        player = [nx, ny]

    # Monster randomly moves
    mx = monster[0] + random.choice([-1, 0, 1])
    my = monster[1] + random.choice([-1, 0, 1])

    if 1 <= mx < WIDTH - 1 and 1 <= my < HEIGHT - 1:
        if dungeon[my][mx] != "#":
            monster = [mx, my]

    # Fight
    if player == monster:
        print("\n⚔️ A monster attacks!")
        health -= 1

        if random.random() < 0.5:
            print("You defeated the monster!")
            monster = [random.randint(2, WIDTH - 3),
                       random.randint(2, HEIGHT - 3)]
        else:
            print("The monster escaped!")

        input("Press Enter...")

    # Treasure
    if player == treasure:
        gold += 100
        draw()
        print("\n🎉 You found the treasure!")
        print(f"You escaped with {gold} gold!")
        break

    if health <= 0:
        draw()
        print("\n💀 You died in the dungeon...")
        break
        DeprecationWarning
        