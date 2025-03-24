"Creating Wordle!"

__author__: str = "730649503"


def contains_char(anylen: str, single_char: str) -> bool:
    "is the character in the string?"
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    index = 0
    while index < len(anylen):
        if anylen[index] == single_char:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    "Emojifying with colored squared on guesses"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        index += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    "Inputting a certain length word"
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """Putting everything together"""
    turns: int = 1
    max_turns: int = 6
    won: bool = False
    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="sissy")
