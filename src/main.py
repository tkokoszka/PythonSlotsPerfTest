import argparse

from all_scenarios import ALL_SCENARIOS
from log import configure_logger
from reporter.text_table import TextTableReporter
from runner.run import run_scenarios

DEFAULT_NUM_INSTANCES = 100_000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Benchmark memory and CPU cost of Python data structures",
    )
    parser.add_argument(
        "-n",
        "--num-instances",
        type=int,
        default=DEFAULT_NUM_INSTANCES,
        help=f"number of instances to create per scenario (default: {DEFAULT_NUM_INSTANCES:_})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logger()
    executions_stats = run_scenarios(ALL_SCENARIOS, args.num_instances)
    print(TextTableReporter().report(executions_stats))


if __name__ == "__main__":
    main()
