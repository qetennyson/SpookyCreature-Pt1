import random

caves = ["A cave with mysterious lights twinkling inside.", "A cave with an orange, flickering glow.",
         "A cave which shifts about in the waning sun.", "A cave that emanates a haunting howl."]

intros = ["\nYou are Gerald Ames, gravekeeper at the St. Athanasius cemetery in Louisville, KY.  Late one night while\n "
          "tending to the final resting place of so many souls, a bright light shines suddenly from a mausoleum in\n "
          "the Northwest corner of the graveyard.  Suspecting teenage trespassers, you move briskly and quietly to the\n "
          "light, hoping to catch the disrespectful youth unaware.  However, as you get closer you begin to hear a\n "
          "haunting sound.  It sounds like the howl of a lost puppy, but distant and strange as though it were stuck\n "
          "in a barrel.  The light has become brighter in your approach.  An icy grip envelops your stomach,\n "
          "and just as you are about to run away in the other direction an invisible hook takes you by the neck.  You\n "
          "are pulled into the light violently, and the world around you disappears.\n"]

cave_left = caves.pop(caves.index(random.choice(caves)))
cave_right = random.choice(caves)

bad_creatures = ["The Corpses of a 90's Boy Band", "Moderately Agitated Dragons",
                 "Teenage Unicorns", "A Bag of Angry Cats"]

good_creatures = ["a Friendly Ghost", "a Golden Dragon", "Seven Dwarves",
                  "a warm chocolate chip cookie that reads to you", "John Denver's anthropomorphized guitar"]

SLEEP = 3


def show_caves():
    print(f"1. {cave_left}")
    print(f"2. {cave_right}")
    print('\n')


def choose_cave(p_choice):
    choice = p_choice[0]
    return int(choice)


def check_cave(bad_cave, cave):
    return bad_cave == cave


def print_intro():
    print(random.choice(intros))


def print_header():
    print("**************************************")
    print("  WELCOME... TO SPOOPY CREATURE CAVES")
    print("**************************************")


def print_outro(win):
    if win:
        print("\nYou win.")
    else:
        print("\nYou lose.")


def main():
    while True:
        print_header()

        start = input("Enter [start] to begin, or [Q] to quit: ")
        bad_cave = random.randint(1, 2)
        if start.strip().lower()[0] == 's':
            print_intro()

            print(f"A mysterious figure appears before you and offers you a choice, "
                  f"you must traverse a spooky cave.\n")

            show_caves()

            cmd = input("What cave do you choose? (1 or 2) ")

            if check_cave(bad_cave, choose_cave(cmd)):
                print_outro(False)
            else:
                print_outro(True)
        else:
            print("2spoopy4u.")


if __name__ == '__main__':
    main()
