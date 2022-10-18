# Merging intervals
MergeIntervals is a package for merging intervals.\
Given a list of intervals, return a list of intervals, which are not overlapping. \
Assuming
- integers only, 
- input is not an empty list,
- correct intervals -> e.g. no ```[9, 4]```.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

```python
from MergeIntervals import merge_intervals

# returns [[2, 23], [25, 30]]
interval_test = [[25, 30], [2, 19], [14, 23], [4, 8]]
merge_intervals(interval_test)
```

## Testing
The package ```pytest``` is needed. Run pytest in the terminal:
```bash
pytest
```


