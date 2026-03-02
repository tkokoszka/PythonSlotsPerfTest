import argparse

from all_scenarios import ALL_SCENARIOS
from log import configure_logger
from reporter.comparison_table import ComparisonTableReporter
from reporter.results_table import ResultsTableReporter
from runner.run_with_trials import run_scenarios_with_trials


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Benchmark memory and CPU cost of Python data structures",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--num-instances",
        type=int,
        default=100_000,
        help="number of instances to create per scenario",
    )
    parser.add_argument(
        "-t",
        "--trials",
        type=int,
        default=10,
        help="number of trials per scenario",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logger()
    executions_stats = run_scenarios_with_trials(
        ALL_SCENARIOS, args.num_instances, args.trials
    )
    print(ResultsTableReporter().report(executions_stats))
    print(ComparisonTableReporter("results_size_ram_bytes").report(executions_stats))


if __name__ == "__main__":
    main()
