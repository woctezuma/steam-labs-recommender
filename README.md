# Steam Labs Recommender

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

![Interactive Recommender](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/banner.png)

This repository contains Python code to tweak the [Interactive Recommender](https://store.steampowered.com/recommender/) of [Steam Labs](https://store.steampowered.com/labs).

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

TODO:
-   average ranking,
-   reverse-engineer the formula,
-   estimate the popularity by cross-referencing data.

## References

-   Posts on ResetERA to figure out the meaning of:
    - [the variables](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22706382),
    - [some interpolation javascript code](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22707917),
-   Explanations regarding the interpolation of rankings: [here](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22709362) and [there](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22709744),
-   [A tweak](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22710041) to filter any of the 337 tags with the current Interactive Recommender.

<!-- Definitions -->

[build]: <https://travis-ci.org/woctezuma/steam-labs-recommender>
[build-image]: <https://travis-ci.org/woctezuma/steam-labs-recommender.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/steam-labs-recommender/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/steam-labs-recommender/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/steam-labs-recommender/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/steam-labs-recommender>
[codecov-image]: <https://codecov.io/gh/woctezuma/steam-labs-recommender/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/steam-labs-recommender>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/34f2fd74cb344d79ae4a6d51746ec987>

