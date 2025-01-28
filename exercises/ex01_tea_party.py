"""ex01_tea_party"""

"""Writing multiple small functions that each solve a single problem"""
"""Writing functions that call other functions"""
"""Writing a "main" function that orchestrates the program's execution"""


__author__: str = "730461167"


def main_planner(guests: int) -> None:
    """Brings together all functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), int((treats(guests))))))
    return None


def tea_bags(people: int) -> int:
    """Determines the amount of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Determines the amount of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost of tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
