import humanize

from dataclass_regular import create_dataclasses
from dataclass_slots import create_dataclasses_slots
from measure_res import measure


def main():
    num_cycles = 1_000_000

    def _fun_dataclass():
        nonlocal num_cycles
        return create_dataclasses(num_cycles)

    def _fun_dataclass_slots():
        nonlocal num_cycles
        return create_dataclasses_slots(num_cycles)

    print(f"### Running {humanize.intcomma(num_cycles)} cycles")
    measure("dataclass_slots", _fun_dataclass_slots)
    measure("dataclass", _fun_dataclass)


if __name__ == "__main__":
    main()
