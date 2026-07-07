from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda t, p: (spell1(t, p), spell2(t, p))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda t, p: base_spell(t, multiplier * p)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda t, p: spell(t, p) if condition(t, p) is True else "Spell" \
                                                                    " fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda t, p: [spell(t, p) for spell in spells]


def main():
    print("\x1b[2J\x1b[H")
    print("\x1b[42m")
    print("Testing spell combiner...\x1b[0m")
    print("Combined spell result:")
    for x in (spell_combiner(
        lambda t, p: f"Fireball hits {t}",
        lambda t, p: f"Heals {t}")
        ("Dragon", 10)): print(x, end=', ')
    print("\x1b[42m")
    print("Testing power amplifier...\x1b[0m")
    print("Amplified spell result bla bla...")
    print("\x1b[42m")
    print("Testing conditional caster...\x1b[0m")
    print("Combined spell result bla bla...")
    print("\x1b[42m")
    print("Testing spell sequence...\x1b[0m")
    print("Combined spell result bla bla...")


if __name__ == "__main__":
    main()
