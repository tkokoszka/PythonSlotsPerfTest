from all_scenarios import ALL_SCENARIOS
from log import configure_logger
from reporter.text_table import TextTableReporter
from runner.run import run_scenarios


def main():
    configure_logger()
    executions_stats = run_scenarios(ALL_SCENARIOS, 100_000)
    print(TextTableReporter().report(executions_stats))


if __name__ == "__main__":
    main()
