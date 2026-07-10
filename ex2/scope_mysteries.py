from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def add():
        nonlocal count
        count += 1
        return count
    return add


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def acc(pow: int):
        nonlocal power
        power += pow
        return power
    return acc


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item: str):
        return f"{enchantment_type} {item}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    data = {}

    def store(key: str, value: str) -> None:
        # nonlocal data
        data.update({key: value})

    def recall(key: str) -> str:
        if key in data:
            return data[key]
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}\n")
    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}\n")
    print("Testing enchantment factory...")
    enflame = enchantment_factory("Flaming")
    freeze = enchantment_factory("Frozen")
    print(enflame("Sword"))
    print(freeze("Shield"), end='\n\n')
    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']("secret", "42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
