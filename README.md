# Whistletips: Go woop woop!
## boto3/AWS helper library + AWS tools

# Requirements

pip:
 - boto3

# Installation

```
./setup.py install
```

# Usage

## wt-lb

```
(venv) #$ ./wt-lb.py qa1
['qa1-web-1', 'qa1-web-0']
(venv) #$ ./wt-lb.py qa1 --rm qa1-web-1
(venv) #$ ./wt-lb.py qa1
['qa1-web-0']
(venv) #$ ./wt-lb.py qa1 --add qa1-web-1
(venv) #$ ./wt-lb.py qa1
['qa1-web-1', 'qa1-web-0']
(venv) #$
```

# Developing

Fork, make changes, and send pull request. Run `./setup.py flake8` to make sure it's clean.

# TODO

Add test cases.

# License

[Unlicense](LICENSE) (Public domain)
