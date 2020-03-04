animals = [("cow", "mooooo "), ("bear", "growl "),
           ("dog", "bark "), ("duck", "quack "), ("horse", "neigh ")]


for animal, sound in animals:
    here = "here a " + sound
    there = "there a " + sound
    witha = "with a " + sound + sound + " here "
    anda = "and a " + sound + sound + "there "
    everywhere = "everywhere a " + sound + sound + ".  "
    old = "Old Mcdonald had a farm EIEIO "
    onthat = "and on that farm he had a " + animal + ", EIEIO "
    print(old + onthat + witha + anda + here + there + everywhere + old)
