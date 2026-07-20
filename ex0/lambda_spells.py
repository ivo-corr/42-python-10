# from data_generator import FuncMageDataGenerator
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, int]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int) -> list[dict[str, str]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* '+x+' *', spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    result: dict[str, int | float] = {}
    result["max_power"] = max(map(lambda x: x["power"], mages))
    result["min_power"] = min(map(lambda x: x["power"], mages))
    result["avg_power"] = round(
        sum(map(lambda x: x['power'], mages))/len(mages), 2)
    return result


def main() -> None:
    print("\x1b[2J\x1b[H")
    artifacts = [{'name': "Gandalf",
                  'power': 15,
                  'type': "Mage"},
                 {'name': 'Frodo',
                  'power': 200,
                  'type': 'Frodo'},
                 {'name': 'Garfield',
                  'power': 99999,
                  'type': 'Yes'}
                 ]
    spells = ["Spellerino", 'Spell number 2', "Hello im a spell"]
    # artifacts = FuncMageDataGenerator.generate_artifacts(5)
    # spells = FuncMageDataGenerator.generate_spells(10)
    sorted = artifact_sorter(artifacts)
    print("\x1b[42m\x1b[30m")
    print("Testing artifact sorter...\x1b[0m")
    # [print(f"{a['name']} ({a['power']} power) comes before ")
    # for a in sorted[:1]]
    # [print(f"{a['name']} ({a['power']} power).") for a in sorted[1:-1]]
    # [print(f"{a['name']} ({a['power']} power) who comes before ") for
    # a in sorted[-1]]

    for a in sorted:
        if (sorted.index(a) == 0):
            print(f"{a['name']} ({a['power']} power) comes before ")
        elif (sorted.index(a) == len(sorted) - 1):
            print(f"{a['name']} ({a['power']} power).")
        else:
            print(f"{a['name']} ({a['power']} power) who comes before ")
    pfilter = 100
    print("\x1b[42m\x1b[30m")
    print("Testing power filter... "
          f"[artifacts with power >= {pfilter}]\x1b[0m")
    [print(f"{a['name']} ({a['power']} power)")
     for a in power_filter(artifacts, pfilter)]
    print("\x1b[42m\x1b[30m")
    print("Testing spell transformer...\x1b[0m")
    [print(x, end=' ') for x in spell_transformer(spells)]
    print("\n\x1b[42m\x1b[30m")
    print("Testing mage stats...\x1b[0m")
    print(mage_stats(artifacts))


if __name__ == "__main__":
    main()
