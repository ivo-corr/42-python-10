from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
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


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


@singledispatch
def spell_dispatcher(value: Any) -> Callable[[Any], str]:
    print("Unknown spell type")


@spell_dispatcher.register(int)
def _(spell: int):
    print(f"Damage spell: {spell} damage")


@spell_dispatcher.register(str)
def _(spell: str):
    print(f"Enchantment: {spell}")


@spell_dispatcher.register(list)
def _(spell: list):
    print(f"Multi-cast: {len(spell)} spells")


def main() -> None:
    data = [[40, 30, 20, 10],
            [f := lambda power, element, target: (
                f'Power={power}, Element={element}, Target={target}'),
             partial_enchanter(f)],
            [0, 1, 10, 15]]
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
    [print(f"Fib ({n}): {memoized_fibonacci(n)}") for n in data[2]]
    print()
    # print(memoized_fibonacci.cache_info())
    print("Testing spell dispatcher...")
    spell_dispatcher(42)
    spell_dispatcher("fireball")
    spell_dispatcher(["fireball", "waterball", "Yes"])
    spell_dispatcher(42.42)


if __name__ == "__main__":
    main()
