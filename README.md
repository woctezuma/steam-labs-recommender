# Steam Labs Recommender

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

![Interactive Recommender](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/banner.png)

This repository contains Python code to tweak the [Interactive Recommender](https://store.steampowered.com/recommender/) of [Steam Labs](https://store.steampowered.com/labs).

## Introduction

The "Interactive Recommender" is a tool provided by Valve on July 11, 2019 to suggest personalized game recommendations.

The input is:
-   the user's 50 most played games, along with [normalized](https://steamcommunity.com/groups/SteamLabs/discussions/3/1643168364649465639/) playtime, last play date, counter of the last played games,
-   minimal external information about the game ([the release date](https://steamcommunity.com/games/593110/announcements/detail/1612767708821405787)).

A neural network predicts the probability that a game is the next purchase of this user, based on the data available for
millions of other users.

The output of the neural network is transformed with an unknown formula to give more or less importance to:
-   popularity,
-   release recency.

It is likely that the release recency is simply used with a threshold to filter out older games.

Regarding [popularity](https://steamcommunity.com/groups/SteamLabs/discussions/3/1643168364649665178/), the formula could be: 
> tweaked_output = neural_network_output + popularity_bias * popularity

The tweaked output are then scaled, so that the top recommendation is always assigned the score of 1000. The scale is stored.
> tweaked_output = score_scale * score

Sorting the scores provide a ranking of game recommendations personalized to the user's data.

## Data

Data personalized to my Steam profile is available in the [`data/`](data/) folder.

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

## Trivia

### Interpolation

There are 30 different pre-computed recommendation rankings of 200 games (`algorithm_options`) for the combinations of:
-   5 popularity biases,
-   6 release recency biases.
The slider combinations of the "Interactive Recommender" results in [an interpolation](https://github.com/woctezuma/steam-labs-recommender/wiki/Interpolation) of the 4 closest rankings:
It is a nice trick to allow people to play with the sliders:
-   without giving too much information away, especially the formula and the popularity values for each game,
-   without overloading the browser with data. There are 30 rankings instead of 101x101.
 
### Misleading sliders

Due to ranking interpolation, sliders can be misleading.
For instance, the recommendations for the past 10 years do NOT include the recommendations for the past 6 months.

![Slider for release recency](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/release_recency_slider.png)

### How to filter rankings with any tag

In order not to overwhelm people with [337 tags](https://gist.github.com/woctezuma/f80d1beec6a26fbb92eb16927c682dc7), most tags are not displayed in the drop-down menu.
However, you can manually add them, and the "Interactive Recommender" will work perfectly fine with them!
All you need is the id for the tag of interest in the HTML page of the "Interactive Recommender". For instance:

![Manually add a tag id](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/tag_input.png)

![Output filtered by tag](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/tag_output.png)
 
Caveat: if nothing appears, then do not forget to move the sliders. You might have a recommendation in one of the other
pre-computed rankings. Due to ranking interpolation, you may have to fiddle with the sliders for a new game to pop in.
 
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

