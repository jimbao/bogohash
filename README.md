# Hash is fast, hash is cool



## Benefits

- Fast
- Consistent
- Not sensitive to brute force attacks
- Has so many neat properties! For any strings x and y, where H() is the bogohash function and "+" is concatenation, all of these things are true:
    - H(x)+H(y) = H(y)+H(x)
    - H(x)+H(y) = H(x+y)
    - H(x+y) = H(y+x)
    - H(x+0) = H(x) (where 0 is empty input data)

## Flaws

- Many hash collisions Q(' .')-O
- For large input data sizes, the hash may be inconveniently large

## Installation

It's not recommended to install this package. But if you read this far, why not.

```pip install bogohash```

## Usage

```python
import bogohash

myhash = bogohash.bogo("password")
digest = myhash.digest()
```
