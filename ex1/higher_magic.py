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
    results = [spell_combiner(
        lambda t, p: f"Fireball hits {t}",
        lambda t, p: f"Heals {t}")("Dragon", 10),
        [lambda t, p: p, power_amplifier(lambda t, p: p, 3)],
        [conditional_caster(
            lambda t, p: p > 10 and t != 'Dragon',
            lambda t, p: f"Fireball hits {t} with power {p}")("Warrior", 15),
         conditional_caster(
            lambda t, p: p > 10 and t != 'Dragon',
            lambda t, p: f"Fireball hits {t} with power {p}")("Dragon", 15)],
        [s1 := lambda t, p: f"Fireball hits {t} with power {p}",
         s2 := lambda t, p: f"Iceball hits {t} with power {p}",
         lambda t, p: f"Thunder hits {t} with power {p}",
         spell_combiner(s1, s2)]
        ]
    # print("\x1b[2J\x1b[H")
    print("\x1b[42m")
    print("Testing spell combiner...\x1b[0m")
    print("Combined spell result:")
    for x in results[0]:
        print(x, end=', ') if x != results[0][-1] else print(x)
    print("\x1b[42m")
    print("Testing power amplifier...\t[multiplier: 3x]\x1b[0m")
    print("Amplified spell result:")
    print(f"Original: {results[1][0]('Dragon', 10)}, Amplified: "
          f"{results[1][1]('Dragon', 10)}")
    print("\x1b[42m")
    print("Testing conditional caster...\t"
          "[Condition p > 10 and t != 'Dragon']\x1b[0m")
    print("\x1b[32mPositive conditional caster result:")
    print(results[2][0])
    print("\x1b[31mNegative conditional caster result:")
    print(results[2][1])
    print("\x1b[42m")
    print("Testing spell sequence...\t"
          "[3 simple spells and a combined spell]\x1b[0m")
    print("Spell sequence result:")
    [print(x) for x in spell_sequence(results[3])("Dragon", 25)]


if __name__ == "__main__":
    main()
