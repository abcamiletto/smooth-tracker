from smooth_tracker import SmoothTracker


def test_tracker_init():
    tracker = SmoothTracker()
    assert tracker is not None
