# Data

This repository contains data personalized to my Steam profile.

## Source

The data can be found on the [Interactive Recommender](https://store.steampowered.com/recommender/) page.
It is at the top of the HTML code of the page.
I have copied each of the four variables into different .json files.

![Data source](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data.png)

## Variables

-   `gAppInfo.json` contains a dictionary matching app ids to app info available on the Steam store:
    - n: app name,
    - r: release date (in Unix time),
    - t: tags associated with the app,
    - o: whether the app is owned by the user,
    - w: whether the app is "wishlisted" by the user,
    - i: whether the app is marked as "ignored" by the user.

```javascript
window.gAppInfo = {
  "363970": {
    "n": "Clicker Heroes",
    "r": 1431565500,
    "t": [ 9, 21, 113, 122, 492, 597, 599, 1684, 3859, 3871, 4136, 4182, 4190, 5350, 379975
    ],
    "o": true
  },
  [...]
  "1059150": {
    "n": "Ritual: Crown of Horns",
    "r": 1558094437,
    "t": [ 19, 492, 493, 1647, 1734, 1756, 1774, 4026, 4182, 4345, 4637, 4667
    ]
  }
};
```

-   `gInputApps.json` contains a list of info about my 50 most played Steam games, which is the algorithm input:
    - n: counter of the last played games ; the most recently played game is assigned 0, the previous one 1, etc.
    - a: app id,
    - p: playtime (in hours),
    - l: date when the game was last played (in Unix time).

```javascript
window.gInputApps = [
  {
    "n": 38,
    "a": 570,
    "p": 3707,
    "l": 1555954754
  },
  [...]
  {
    "n": 470,
    "a": 278100,
    "p": 19,
    "l": 1496011976
  }
];
```

-   `gRecommendations.json` contains a list of 30 recommendation rankings, which is the algorithm output:
    - setting "algorithm_variant", currently useless (as it is always set to 0), to switch between recommender versions,
    - "popularity" bias, which takes one of 5 values (-1/3, 0, 1/3, 2/3 and 1),
    - "release recency" bias, which takes one of 6 values (120, 60, 36, 24, 12, and 6 months),
    - setting "include_already_played_in_results" to choose whether to filter out games owned by the user,
    - score scale, so that the normalized score of the top recommendation is always equal to 1000,
    - there are 200 recommended `app_ids`, sorted according to their normalized `scores`. 

```javascript
window.gRecommendations = [
  {
    "algorithm_options": {
      "algorithm_variant": 0,
      "popularity_bias": "-0.333333343267440796",
      "release_recency_bias": "120",
      "include_already_played_in_results": 0
    },
    "recommended_apps": [],
    "score_scale": "0.008876836858689785",
    "app_ids": [ 363970, 247080, 49520, [...] 409690, 373970, 560380 ],
    "scores": [ 1000,  903,  822,  [...] 106, 106, 105 ]
},
[...]
{
  "algorithm_options": {
    "algorithm_variant": 0,
    "popularity_bias": "1",
    "release_recency_bias": "6",
    "include_already_played_in_results": 0
  },
  "recommended_apps": [],
  "score_scale": "0.0626560673117637634",
  "app_ids": [ 933390, 781990, 504620, [...] 840430, 1034900, 1059150 ],
  "scores": [ 1000, 903, 673, [...] 16, 16, 16 ]
  }
];
```

-   `gTags.json` contains a dictionary matching tag ids to tag names for store tags which arise in your recommendations,

```javascript
window.gTags = {
  "9": "Strategy",
  "21": "Adventure",
  "113": "Free to Play",
  [...]
  "8093": "Minigames",
  "5230": "Sequel",
  "6276": "Inventory Management"
};
```
