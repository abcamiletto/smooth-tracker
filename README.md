# Smooth Tracker
Do you have a single-frame whatever? Optimize it over time with a simple tracker made for humans

Designed to be simple yet effective, smooth tracker allows you to smooth you single-frame prediction of whatever you want over time. It works with bounding boxes, keypoints, any numpy-like array.

It implements a second order linear filter, which is a simple way to smooth your predictions.

## Installation

The package is available on pypi, so you can install it with pip:

```bash
    pip install smooth-tracker
```

## Usage Example

Down below we have a quick overview of example scripts. For more details, please refer to the [documentation](https://smooth-tracker.readthedocs.io/en/latest/).

### Tracking a 2D/3D point

Let's start with the simplest example tracking a single point codified as a numpy.ndarray.


```python
from smooth_tracker import SmoothTracker

tracker = SmoothTracker()

while True:
    # Get your prediction
    prediction: np.ndarray
    prediction = get_prediction()  

    # Update the tracker
    smoothed_prediction = tracker.update(prediction)

```

### Tracking multiple 2D/3D point

NB: This is not yet implemented

Let's say you have a prediction of multiple points in 2D. Let's suppose we have a way to recognize them and associate them with a name. We can use a dictionary to store them.


```python
from smooth_tracker import SmoothTracker

tracker = SmoothTracker()

while True:
    # Get your prediction
    names: list[str] 
    predictions: list[np.ndarray]
    names, predictions = get_prediction()

    # Update the tracker
    smoothed_prediction = tracker.update(predictions, names=names)

```

### Tracking multiple 2D/3D point, without names

NB: This is not yet implemented

In the case we have no way of identifying the prediction, we can let the tool trace back the correspondance based on the previous positions.

```python
from smooth_tracker import SmoothTracker

tracker = SmoothTracker(auto_names=True)

while True:
    # Get your prediction
    predictions: list[np.ndarray]
    predictions = get_prediction()

    # Update the tracker
    smoothed_prediction = tracker.update(predictions)

```


### TODOs

- [ ] Add a way to track multiple points with names
- [ ] Add a way to track multiple points without names
- [ ] Does it make enough to use a KF? Answer plz
