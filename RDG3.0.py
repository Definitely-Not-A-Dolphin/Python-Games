NumberInput = input("Welcome to the RDG, the Random Death Generator.\nLet's see how you are going to die! Would you like a random death or a number labeled one? Type 'Random' or 'Number': ")

ListDeaths = [
    "A great fall from the stairs.",
    "The impact of a meteor on your very large forehead.",
    "Drowning in a pond of 15 centimeters deep, because you got an epilelpsy attack. The flashing reflectations of the sun triggered it.",
    "Starving to death after you tried to hide in a closet from a serial killer. You accidentally locked yourself in.",
    "Noclipping through the floor and ended up in the backrooms. A monster killed you.",
    "Poisoning yourself with an orange.",
    "Laughing non-stop for 30 minutes, you died from a heart attack.",
    "Exploding chewing gum.",
    "Getting pinned by an uncut sushi roll.",
    "Getting hit by rolling wheels of parmesan cheese.",
    "Exploding. There was a piece of dynamite inside of your birthday cake.",
    "Looking through the barrel of your shotgun to see what was wrong.",
    "Tripping and landing face first into wet concrete.",
    "The impact of a soda can on your private parts after being dispensed at a speed of 140 kilometers an hour",
    "Burger King Foot Lettuce.",
    "Eating a living pufferfish for a dare.",
    "Getting boiled in a barrel filled with vanilla extract.",
    "An aborting at the age of 20 years old.",
    "The stopping of your life support. Your grandchildren thought it was enough for now.",
    "A very hungry catarpillar.",
    "Your cat sitting on your face while you were asleep.",
    "Sniffing to much glue.",
    "Misgendering the purple-blue haired girl in your class (they/them)",
    "Falling into a sinkhole underneath your house.",
    "Chocking on an ice cube.",
    "Eating a lemon peel.",
    "Voting for Forum voor Democratie.",
    "Getting bounty hunted for exactly 23 dollars and 87 cents."
]

if(NumberInput == "Random"):
    import random
    DeathNumber = random.randint(0,27)

if(NumberInput == "Number"):
    while True:
        try:
            DeathNumber = int(input(">\nPlease insert a number from 1 to 28: ")) -1
            if DeathNumber > len(ListDeaths) or DeathNumber < 0:
                raise ValueError()
            break
        except ValueError:
            print("Thats not a valid input you dummy")

print(">\nYou died from:", (ListDeaths[DeathNumber]))