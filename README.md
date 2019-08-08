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

NB: It is not known whether the input is really limited to the 50 most played games.
It is [possible](https://metacouncil.com/threads/metasteam-july-2019-racing-towards-empty-wallets.1278/page-34#post-66967) that the whole game library is actually taken into account, and that the 50 most played games only appear on the Recommender webpage for cosmetic purposes.

A neural network predicts the probability that a game is the next purchase of this user, based on the data available for
millions of other users.

The output of the neural network is transformed with an unknown formula to give more or less importance to:
-   [popularity](https://steamcommunity.com/groups/SteamLabs/discussions/3/1643168364649665178/),
-   release recency.

The most basic assumption for this formula would be such as:
> tweaked_output = neural_network_output + popularity_bias * popularity + release_recency_bias * release_recency

It is likely that the release recency is simply used with a threshold to filter out older games.
In this case, the suggested formula would be instead: 
> tweaked_output = neural_network_output + popularity_bias * popularity

The tweaked outputs are then scaled, so that the top recommendation is always assigned the score of 1000. The scale is stored.
> tweaked_output = score_scale * score

Sorting the scores results in a ranking of game recommendations personalized to the user's data.

## Data

Data personalized to my Steam profile is available in the following folders:
-   [`data/`](data/),
-   [`data_v2/`](data_v2/) after [the update](https://steamcommunity.com/groups/SteamLabs/discussions/3/1643170269567305036/) shipped on July 27, 2019,
-   [`data_v3/`](data_v3/) after [the update](https://steamcommunity.com/groups/SteamLabs/discussions/3/1643170903484574354/) shipped on August 8, 2019.

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Download the inputs and results of the recommender

You could manually download the inputs and results of the recommender to `data_v2/`.
Otherwise, this process can be automated after providing the following personal information:

1.   Fill-in your SteamID in the function `get_steam_id()` found in `utils.py`.

2.   Fill-in your cookie information in a new file called `personal_info.json`:

```json
{
  "sessionid": "PASTE_YOUR_COOKIE_VALUE_HERE",
  "steamLoginSecure": "PASTE_YOUR_COOKIE_VALUE_HERE"
}
```

### TODO

TODO:
-   average ranking,
-   reverse-engineer the formula,
-   estimate the popularity by cross-referencing data.

## Trivia

### Interpolation

There are 30 pre-computed recommendation rankings of 200 games (`algorithm_options`) for the combinations of:
-   5 popularity biases,
-   6 release recency biases.

A combination of sliders of the "Interactive Recommender" leads to [an interpolation](https://github.com/woctezuma/steam-labs-recommender/wiki/Interpolation) of the 4 closest rankings.
If a game appears in a ranking but not in the 3 others, its score is set to 0 for the 3 other rankings, and the interpolation is then computed.

It is a nice trick to allow people to play with the sliders:
-   without giving too much information away, especially the formula and the "popularity" values for each game,
-   without overloading the browser with data. There are 30 rankings instead of 101x101.

Moreover, it is important to notice that the interpolation is bilinear, which is consistent with the linear formula
mentioned above for `tweaked_output` with respect to the popularity bias.
However, with respect to the release recency bias, it might be a hack ; further investigations would be required to figure it out.

### Misleading sliders

Sliders can be misleading, especially if you filter rare tags.

For instance, recommendations for the past 10 years do NOT necessarily include recommendations for the past 6 months.

![Slider for release recency](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/release_recency_slider.png)

This is a consequence of cutting the pre-computed rankings after 200 entries, and then interpolating rankings.

### How to filter rankings with any tag

In order not to overwhelm people with [337 tags](https://gist.github.com/woctezuma/f80d1beec6a26fbb92eb16927c682dc7), most tags are not displayed in the drop-down menu.

However, you can manually add them, and the "Interactive Recommender" will work perfectly fine with them!
All you need is the id for the tag of interest in the HTML page of the "Interactive Recommender". For instance:

![Manually add a tag id](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/tag_input.png)

![Output filtered by tag](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/tag_output.png)
 
Caveat: if nothing appears, then do not forget to move the sliders.
Indeed, you might have a recommendation in one of the other pre-computed rankings, and due to ranking interpolation, you
would have to fiddle with the sliders for a new game to pop in.

**Edit**: Tag filtering was officially extended to every tag with the update shipped on August 8, 2019.

![Extended tag filtering](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/tag_filtering.png)

## Pieces of advice

-   Setting the slider to "popular" is mostly useful for new Steam users.

Looking for "popular" games makes sense for new Steam users.
However, for long-time users, you likely know about the surfaced "popular" games, and discarded them for good reasons.
Looking for more "niche" games increases the chance to discover a game which you might want to purchase and play.

![Optimal popularity slider position](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/optimal_popularity_slider.png) ![Optimal popularity slider value](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/optimal_popularity_slider_value.png)

-   The recommender might be biased by game bundles.

The recommender might be biased by game bundles.
Indeed, a few games could get recommended solely because they appeared in a bundle along with games which you own.
Focusing on recent releases (max 2-3 years) should alleviate this issue, because recent games are less likely to
have been featured in many bundles.

![Optimal release recency slider position](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/optimal_release_recency_slider.png) ![Optimal release recency slider value](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/optimal_release_recency_slider_value.png)

For instance, I suspect that the game "Steel Rats" is recommended to me because it was featured in a Humble Monthly
bundle along with two games (MINIT and Dandara) which I have purchased with [Group Buys](https://steamcommunity.com/groups/groupbuys/) and then played.
That being said, I might be overestimating the impact of this issue, which may be toned down if the Recommender really
only considers my 50 most played games, which do not include any of these two games.

![Humble Monthly Bundle](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/monthly.png)

## Extent of the input data

On April 27, 2019, Valve shipped an update which allows to exclude games from the input data.
This allows us to figure out whether the input data is limited to the top 50 games, or if it is larger, potentially
up to the whole user library.

I have tried the recommender with a smurf account which has:
-   three games (Dota2, Chivarly, Mirage),
-   non-zero playtime only for Dota2.

As a first observation, the list shown on the left of the recommender only includes Dota2.
This confirms that, at least cosmetically, owned games with zero playtime are ignored.

Second, if Dota2 is manually excluded from the input data, then there is no recommendation at all.
This shows that:
-   there is no default recommendation,
-   games with zero playtime are effectively ignored.

![Void response if the input is empty](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/void_response.png)

Now, if I go back to my main account, and manually exclude all of the top 50 games from the input data,
there are still recommended games.
This implies that the input data is not empty, and thus a bigger part of my library had to be taken into account.

In conclusion, the recommender is fed more than your top 50 games, likely your whole library data
(with positive playtime), including all of these idled games.

## References

-   Posts on ResetERA to figure out the meaning of:
    - [the variables](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22706382),
    - [some interpolation javascript code](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22707917),
    - [the updates shipped on July 27, 2019](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-53#post-23105410),
-   Explanations regarding the interpolation of rankings: [here](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22709362) and [there](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22709744),
-   [A tweak](https://www.resetera.com/threads/pc-gaming-era-july-2019-life-liberty-and-the-pursuit-of-richaaaaaaard.126544/page-31#post-22710041) to filter any of the 337 tags with the current Interactive Recommender,
-   [An article on PC Gamer](http://www.pcgamer.com/this-algorithm-picks-out-steams-best-hidden-gems/) which provides nice insights regarding my approach to [discover hidden gems](https://github.com/woctezuma/hidden-gems).

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
