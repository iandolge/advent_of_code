import pytest  # noqa: F401

from day_01 import part_one, part_two


def pytest_addoption(parser):
    parser.addoption("")


@pytest.fixture
def demo_input():
    with open("demo-input.txt") as f:
        return f.read()


def test_part_one(demo_input):
    assert part_one(demo_input) == 24000


def test_part_two(demo_input):
    assert part_two(demo_input) == 45000
