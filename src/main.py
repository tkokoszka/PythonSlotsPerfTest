from dataclass_regular import create_dataclasses
from dataclass_slots import create_dataclasses_slots
from measure_res import measure


def main():
    def _fun1():
        return create_dataclasses(10_000_000)

    def _fun2():
        return create_dataclasses_slots(10_000_000)

    r1 = measure("regular", _fun1)
    r2 = measure("slots", _fun2)
    print(f"r1 len={len(r1)}, r2 len={len(r2)}")


if __name__ == "__main__":
    main()
