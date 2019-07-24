# Rangl

Prototype for policy submission (threshold-type policy).



## Getting  started

Prerequisite is python 3.7.

Install dependencies using:

```shell
pip install -r requirements.txt
```



## Typical use

Define a policy in `user.py` then run it using:

```shell
$ ./user.py

DEBUG:rangl:Prediction: t_pred: 17.5, spill_pred:  True
DEBUG:rangl:Output: spill: False, I: 0
DEBUG:rangl:score: -12.0
score: -12.0
DEBUG:rangl:Prediction: t_pred: 15.5, spill_pred:  True
DEBUG:rangl:Output: spill: False, I: 0
DEBUG:rangl:score: -12.0
score: -12.0
DEBUG:rangl:Prediction: t_pred: 13.0, spill_pred:  True
DEBUG:rangl:Output: spill: True, I: 1
DEBUG:rangl:score: 35.0
score: 35.0
DEBUG:rangl:Prediction: t_pred: 17.5, spill_pred:  True
DEBUG:rangl:Output: spill: False, I: 0
DEBUG:rangl:score: -12.0
score: -12.0

...

```



## Contributing

Run the tests using:

```shell
$ pytest -s
Test session starts (platform: darwin, Python 3.7.1, pytest 4.3.1, pytest-sugar 0.9.2)
rootdir: /Users/lmason/Research/Rangl/explore, inifile:
plugins: sugar-0.9.2, nameko-2.11.0
collecting ... Loaded threshold: -2.043060250781589
Loaded TERMINAL: 48.0

 tests/test_rangl.py ✓✓                                         67% ██████▋   
DEBUG:rangl:Prediction: t_pred: 15.5, spill_pred:  True
DEBUG:rangl:Output: spill: False, I: 0
DEBUG:rangl:score: -12.0
 tests/test_rangl.py ✓✓✓                                       100% ██████████

Results (1.06s):
       3 passed
```

