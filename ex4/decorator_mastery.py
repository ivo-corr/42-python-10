from functools import wraps
from typing import Callable
import time
from typing import Any, cast


def power_validator(min_power: int
                    ) -> Callable[[Any], Any]:
    def decorator(func: Callable[[str, int], str]
                  ) -> Callable[[str, int], str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            if cast(int, args[2]) < min_power:
                return "Insufficient power for this spell"
            return (func(*args, **kwargs))
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Any], Any]:
    def decorator(func: Callable[[Any], Any]) -> Callable[[Any, Any], str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for i in range(max_attempts):
                try:
                    result: str = func(*args, **kwargs)
                    return (result)
                except Exception:
                    if i != (max_attempts - 1):
                        print("Spell failed, retring... "
                              f"(Attempt {i + 1} of {max_attempts})")
                    if i == max_attempts - 1:
                        print("Spell casting failed "
                              f"after {max_attempts} attempts")
            return ""
        return wrapper
    return decorator


def spell_timer(func: Callable[[Any, Any], Any]) -> Callable[[str, int], str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"Casting {wrapper.__name__}...")
        start_time: float = time.perf_counter()
        result: str = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        elapsed_time: float = end_time - start_time
        print(f"Spell completed in {round(elapsed_time, 3)} seconds")
        return result
    return wrapper


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) >= 3 and all([s.isalpha() for s in name.split(" ")])):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball(name: str, power: int) -> str:
        time.sleep(0.101)
        return ("Fireball cast!")

    @retry_spell(3)
    def iceball() -> str:
        raise Exception("no no")
        return ("Iceball cast!")
    print("Testing spell timer...")
    print(f"Result: {fireball('Someone', 15)}")
    print("\nTesting retrying spell...")
    iceball()
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G4nd4lf"))
    mg = MageGuild()
    print(mg.cast_spell("Lightning", 15))
    print(mg.cast_spell("Lightning", 8))


if __name__ == "__main__":
    main()
