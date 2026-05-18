import random  # Python standard library import used to simulate nondeterministic test behavior


def test_random_failure():  # simple test intentionally written to illustrate flaky behavior


    assert random.choice(
        [True, False]
    )  # assertion uses random choice to produce either success or failure in Python
