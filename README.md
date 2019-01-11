# Hash is fast, hash is cool



## Benefits

- Fast
- Consistent
- Not sensitive to brute force attacks

## Flaws

- Many hash collisions Q(' .')-O

## Installation

It's not recommended to install this package. But if you read this far, why not.

```pip install bogohash```

## Usage

```python
import bogohash

myhash = bogohash.bogo("password")
digest = myhash.digest()
```
