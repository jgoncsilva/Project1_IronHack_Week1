# define rooms and items
# Objects
couch = {
    "name": "couch",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dinning_table = {
    "name": "dinning table",
    "type": "furniture",
    "description": "There is a paper on the table. You turn it over. There is a message\n ...---..."
}

safe = {
    "name": "safe",
    "type": "safe",
}

bookcase = {
    "name": "bookcase",
    "type": "furniture",
    "description": "A bookcase full of books of all sorts of themes. Python for Beginners, Harry Potter, Lord of the Rings, 50 Shades of...",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
    "description": "So Sweet by beauty queen. But there's no time to sleep"
}

# Main Doors
door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}
# Main Keys
key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}
# Main Bedrooms
game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

snake = {
    "name": "snake",
    "type": "deadly"
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
    "name": "outside"
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]
