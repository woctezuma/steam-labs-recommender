# Data

This repository contains data personalized to my Steam profile.

## Source

The data can be found on the [Interactive Recommender](https://store.steampowered.com/recommender/) page.

After the update on July 27, 2019, the data is obtained via two GET queries:
-   to retrieve `inputs.json`:
```
https://store.steampowered.com/recommender/STEAM_ID/inputs?sessionid=SESSION_ID&steamid=STEAM_ID
```
-   to retrieve `results.json`:
```
https://store.steampowered.com/recommender/STEAM_ID/results?sessionid=SESSION_ID&steamid=STEAM_ID&include_played=0&algorithm=0&reinference=0&model_version=0
```

You can notice parameters other than `sessionid` and `steamid`:
-   `include_played` (`0`),
-   `algorithm` (`0`),
-   `reinference` (`0`),
-   `model_version` (`0`),
-   (optional) `ignored` (a list of ignored appIDs, e.g. `364470,440`),

![Query parameters with ignore feature toggled ON](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/ignore_feature_query_parameters.png)

## Variables

-   `inputs.json` contains the equivalent of `gInputApps.json`:
    - with the addition of a flag `i` (whether the app is marked as "ignored" by the user).

![Inputs](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data_v2_inputs.png)

![Ignore feature](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/ignore_feature.png)

-   `results.json` contains the equivalent of:
    - `gAppInfo.json` in `app_info`,
    - `gRecommendations.json` in `recommendations`,
    - `gTags.json` in `tags`.

![Results](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data_v2_results.png)

