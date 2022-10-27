import pytest
from smooth_tracker import SmoothTracker

from conftest import mono_signals


@pytest.fixture
def tracker():
    return SmoothTracker()


def test_tracker_init():
    tracker = SmoothTracker()
    assert tracker is not None


@pytest.mark.parametrize("sample", mono_signals)
def test_mono_signal(tracker, sample):
    signal = sample["signal"]

    for step in signal:
        prediction = tracker.update(step)

    upper_bound = sample["upper_bound"]
    lower_bound = sample["lower_bound"]

    for component, ub, lb in zip(prediction, upper_bound, lower_bound):
        assert lb <= component <= ub


def test_mono_nan(tracker):
    for i in range(10):
        prediction = tracker.update(None)

    assert prediction is None
