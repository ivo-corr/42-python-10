from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* '+x+' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    pass


def main():
    # artifacts = [{'name': "Gandalf",
    #               'power': 15,
    #               'type': "Mage"},
    #              {'name': 'Frodo',
    #               'power': 200,
    #               'type': 'Frodo'},
    #              {'name': 'Garfield',
    #               'power': 99999,
    #               'type': 'Yes'}
    #              ]
    # spells = ["Spellerino", 'Spell number 2', "Hello im a spell"]
    artifacts = FuncMageDataGenerator.generate_artifacts(5)
    spells = FuncMageDataGenerator.generate_spells(10)
    sorted = artifact_sorter(artifacts)
    print("\x1b[42m\x1b[30m")
    print("Testing artifact sorter...\x1b[0m")
    # [print(f"{a['name']} ({a['power']} power) comes before ") for a in sorted[:1]]
    # [print(f"{a['name']} ({a['power']} power).") for a in sorted[1:-1]]
    # [print(f"{a['name']} ({a['power']} power) who comes before ") for a in sorted[-1]]

    for a in sorted:
        if (sorted.index(a) == 0):
            print(f"{a['name']} ({a['power']} power) comes before ")
        elif (sorted.index(a) == len(sorted) - 1):
            print(f"{a['name']} ({a['power']} power).")
        else:
            print(f"{a['name']} ({a['power']} power) who comes before ")
    pfilter = 100
    print("\x1b[42m\x1b[30m")
    print(f"Testing power filter... [artifacts with power >= {pfilter}]\x1b[0m")
    [print(f"{a['name']} ({a['power']} power)")
     for a in power_filter(artifacts, pfilter)]
    print("\x1b[42m\x1b[30m")
    print("Testing spell transformer...\x1b[0m")
    [print(x, end=' ') for x in spell_transformer(spells)]


if __name__ == "__main__":
    main()