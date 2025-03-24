"For Use Tests and Function Skeletons"

__author__: str = "730649503"


def invert(oed: dict[str, str]) -> dict[str, str]:
    "Switching the keys and the values"
    inverted: dict[str, str] = {}
    for key in oed:
        value = oed[key]
        if value in inverted:
            raise KeyError("Same values detected when inverting dictionary!")
        else:
            inverted[value] = key
    return inverted


def count(oed2: list[str]) -> dict[str, int]:
    "Counting the items in a list"
    counted: dict[str, int] = {}
    idx: int = 0
    while idx < len(oed2):
        value: str = oed2[idx]
        if value in counted:
            counted[value] += 1
        else:
            counted[value] = 1
        idx += 1
    return counted


def favorite_color(oed3: dict[str, str]) -> str:
    "Determining the favorite color"
    colors_list: list[str] = []
    for key in oed3:
        colors_list.append(oed3[key])

    color_counts = count(colors_list)

    max_count = -1
    most_frequent_color = ""

    for key in oed3:
        color = oed3[key]
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_frequent_color = color

    return most_frequent_color


def bin_len(oed4: list[str]) -> dict[int, set[str]]:
    "Bins words by their length into a dictionary"
    bins: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(oed4):
        length = len(oed4[idx])
        if length not in bins:
            bins[length] = set()
        bins[length].add(oed4[idx])
        idx += 1
    return bins
