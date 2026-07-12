from typing import Any, Callable
from functools import reduce, partial, lru_cache
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation.capitalize() == "Add":
        return reduce(lambda x, y: x + y, spells)
    if operation.capitalize() == "Multiply":
        return reduce(lambda x, y: x * y, spells)
    if operation.capitalize() == "Max":
        return reduce(lambda x, y: max(x, y), spells)
    if operation.capitalize() == "Min":
        return reduce(lambda x, y: min(x, y), spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    ps: dict[str, Callable] = {}
    ps.update({"1": partial(base_enchantment, power=50, element="Fire")})
    ps.update({"2": partial(base_enchantment, power=50, element="Water")})
    ps.update({"3": partial(base_enchantment, power=50, element="Air")})
    return ps


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    pass


def main() -> None:
    data = [[40, 30, 20, 10],
            [f := lambda power, element, target: (
                f'Power={power}, Element={element}, Target={target}'),
             partial_enchanter(f)]
]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(data[0], 'add')}")
    print(f"Product: {spell_reducer(data[0], 'multiply')}")
    print(f"Max: {spell_reducer(data[0], 'max')}")
    # print(f"Min: {spell_reducer(data[0], 'min')}")
    print("\nTesting partial enchanter...")
    element: str = "Earth"
    target: str = "Warrior"
    print("Base function app: "
          f"{data[1][0](40, element, target)}")
    [print("Partial function app: "
           f"{data[1][1][k](target=target)}") for k in data[1][1].keys()]

    print("\nTesting memoized fibonacci...")


if __name__ == "__main__":
    main()
