# Pseudorandom number generator with NumPy

## Install:

1. clone/download this repo & `cd` into it
2. make sure you have python and `pipenv` installed on your machine
3. run `$ pipenv install`

## Get your random nums:

This doesn't work yet unless you change `return` to `print` in the function return statement but you can test it (see below)

```
$ pipenv run python app.py
```

## Run tests:

```
$ pipenv run pytest
```

### Check test coverage:

```
$ pipenv run pytest --cov --cov-fail-under=100
```

## Anarchy!

`git commit --no-verify` and `git push --no-verify` to skip pre-commit hooks 😏

### Note:

I have not yet researched the correct conventions for python nor how to structure a python project, please don't hate - this is a work in progress/noobie playground.

## TODO

re-add `__init__.py` where the functions are to use them in `app.py`; move tests to another directory - figure out how to hook up tests to methods in another directory