
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '*'+x+'*', spells))


def mage_stats(mages: list[dict]) -> dict:
    pass


def main():
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
    # print(artifact_sorter(artifacts))
    print(power_filter(artifacts, 20))
    print(spell_transformer(spells))


if __name__ == "__main__":
    main()