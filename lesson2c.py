# Python dictionaries
# hold a collection of keys with their value
# changeable, ordered, no duplicates
# JSON file -> Dictionary (APIs)
# created using braces{}

player = {
    "name": "Jordan",
    # key and its value
    "age": 23,
    "gender": "male",
    "profession": "basketballer",

}
print(player)

# operations
# a. accessing elements
print(player["name"])

x = player.keys()
print(x)
y = player.values()
print(y)
z = player.items()
print(z)

# adding height of the player
player["height"] = 1.87
print(player)

# replacing the name of player
player["name"] = "Michael"
print(player)

# deleting the gender of the player
player.pop("gender")
print(player)