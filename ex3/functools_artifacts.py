from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation.capitalize() == "Add":
        return reduce(lambda x, y: x + y, spells)
    if operation.capitalize() == "Multiply":
        return reduce(lambda x, y: x * y, spells)
    if operation.capitalize() == "Max":
        return reduce(lambda x, y: max(x, y), spells)
    if operation.capitalize() == "Min":
        return reduce(lambda x, y: min(x, y), spells)
    return 0


def partial_enchanter(
        base_enchantment:
        Callable[[int, str, str], str]) -> dict[str, Callable[[str], str]]:
    ps: dict[str, Callable[[str], str]] = {}
    ps.update({"1": partial(base_enchantment, 50, "Fire")})
    ps.update({"2": partial(base_enchantment, 50, "Water")})
    ps.update({"3": partial(base_enchantment, 50, "Air")})
    return ps


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def generic(value: Any) -> str:
        return "Unknown type"

    @generic.register(int)
    def _(spell: int) -> str:
        return (f"Damage spell: {spell} damage")

    @generic.register(str)
    def _(spell: str) -> str:
        return (f"Enchantment: {spell}")

    @generic.register(list)
    def _(spell: list[Any]) -> str:
        return (f"Multi-cast: {len(spell)} spells")
    return generic


def main() -> None:
    def base(power: int, element: str, target: str) -> str:
        return f"Power={power}, Element={element}, Target={target}"
    data = ([40, 30, 20, 10],
            (base,
             partial_enchanter(base)),
            [0, 1, 10, 15])
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
           f"{data[1][1][k](target)}") for k in data[1][1].keys()]

    print("\nTesting memoized fibonacci...")
    [print(f"Fib ({n}): {memoized_fibonacci(n)}") for n in data[2]]
    print()
    # print(memoized_fibonacci.cache_info())
    print("Testing spell dispatcher...")
    dispatcher_system = spell_dispatcher()
    print(dispatcher_system(42))
    print(dispatcher_system("fireball"))
    print(dispatcher_system(["fireball", "waterball", "Yes"]))
    print(dispatcher_system(42.42))


if __name__ == "__main__":
    main()
