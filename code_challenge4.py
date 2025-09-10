# User Input

print("Welcome to the Manga Recommender!")
print("Answer a few questions to get a manga recommendation.")
genre = input("What genre do you like? (Action, Isekai, Slice of Life, Horror)").strip().lower()

# Recommendation Logic
if genre == "action":
    action = input("How long should the manga be? (Short, Medium, Long)").strip().lower()
    if action == "short":
        short = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if short == "2000s":
            print("We recommend 'You Need is Kill'!")
        elif short == "2010s":
            print("We recommend 'Tokyo Ghoul'!")
    elif action == "medium":
        medium = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if medium == "2000s":
            print("We recommend 'Death Note'!")
        elif medium == "2010s":
            print("We recommend 'Assassination Classroom'!")
    elif action == "long":
        long = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if long == "2000s":
            print("We recommend 'One Piece'!")
        elif long == "2010s":
            print("We recommend 'The Seven Deadly Sins'!")
elif genre == "isekai":
    isekai = input("How long should the manga be? (Short, Medium, Long)").strip().lower()
    if isekai == "short":
        short = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if short == "2000s":
            print("We recommend 'The Twelve Kingdoms'!")
        elif short == "2010s":
            print("We recommend 'Drifters'!")
    elif isekai == "medium":
        medium = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if medium == "2000s":
            print("We recommend 'InuYasha'!")
        elif medium == "2010s":
            print("We recommend 'No Game No Life'!")
    elif isekai == "long":
        long = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if long == "2000s":
            print("We recommend 'Fushigi Yugi'!")
        elif long == "2010s":
            print("We recommend 'That Time I Got Reincarnated as a Slime'!")
elif genre == "slice of life":
    slice_of_life = input("How long should the manga be? (Short, Medium, Long)").strip().lower()
    if slice_of_life == "short":
        short = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if short == "2000s":
            print("We recommend 'K-On!'!")
        elif short == "2010s":
            print("We recommend 'The Tatami Galaxy'!")
    elif slice_of_life == "medium":
        medium = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if medium == "2000s":
            print("We recommend 'Honeymoon Salad'!")
        elif medium == "2010s":
            print("We recommend 'Yuri!!! on ICE'!")
    elif slice_of_life == "long":
        long = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if long == "2000s":
            print("We recommend 'Fruits Basket'!")
        elif long == "2010s":
            print("We recommend 'Yotsuba&!'!")
elif genre == "horror":
    horror = input("How long should the manga be? (Short, Medium, Long)").strip().lower()
    if horror == "short":
        short = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if short == "2000s":
            print("We recommend 'Tomie by Junji Ito'!")
        elif short == "2010s":
            print("We recommend 'Ibitsu'!")
    elif horror == "medium":
        medium = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if medium == "2000s":
            print("We recommend 'Highschool of the Dead'!")
        elif medium == "2010s":
            print("We recommend 'Promised Neverland'!")
    elif horror == "long":
        long = input("Which decade do you prefer? (2000s, 2010s)").strip().lower()
        if long == "2000s":
            print("We recommend 'Gantz'!")
        elif long == "2010s":
            print("We recommend 'Parasyte'!")
else:
    print("Sorry, we don't have recommendations for that genre at the moment.")