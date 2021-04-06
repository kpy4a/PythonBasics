from itertools import islice

SUMMARY_FILENAME = "summary.csv"


def add_summary(summary):
    with open(SUMMARY_FILENAME, "a", encoding="utf-8") as f:
        f.write(summary + "\n")


def get_summary_generator():
    with open(SUMMARY_FILENAME, "r", encoding="utf-8") as f:
        for summary in f:
            yield summary.strip()


def get_summary_for_show(from_number, to_number):
    for i, summary in enumerate(islice(get_summary_generator(), from_number, to_number), from_number + 1):
        yield i, summary