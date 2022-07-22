# Data

This repository contains data personalized to my Steam profile.

## Source

The data can be found on the [Interactive Recommender](https://store.steampowered.com/recommender/) page.

After the update on August 8, 2019, the data is obtained via **three** GET queries:
-   to retrieve `tags.json`:
```
https://store.steampowered.com/recommender/STEAM_ID/tags?sessionid=SESSION_ID
```
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
-   (optional) `ignored` (a list of ignored input appIDs, e.g. `364470,440`),

![Query parameters with ignore feature toggled ON](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/ignore_feature_query_parameters.png)

## Variables

-   `tags.json` contains the equivalent of:
    - `gTags.json` (except there are **all the 433 store tags**, not just the ones tailored for your recommended apps).
    
NB: Untying tags from recommendations allows to filter tags even if there is no recommendation attached to them.
Otherwise, some users would not find the tag which they are looking for, wrongly think it is a bug, and ask for a fix.

![Tags](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data_v3_tags.png)

-   `inputs.json` contains the equivalent of `gInputApps.json`:
    - with the addition of a field `t` (for "title"), which contains the **app name** (so that it can be displayed if mouse-hovering).
    - with the addition of a flag `i` (whether the app is marked as "ignored" by the user).
    - with the addition of a flag `ip` (?).

![Inputs](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data_v3_inputs.png)

![Game name displayed when hovering](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/name_hovering.png)

-   `results.json` contains the equivalent of:
    - `gAppInfo.json` in `app_info`,
    - `gRecommendations.json` in `recommendations`, except:
        - there are **400 apps per ranking** instead of 200,
        - `recommended_apps` has been renamed to `recommended_apps_deprecated` (and thus deprecated).

![Results](https://raw.githubusercontent.com/wiki/woctezuma/steam-labs-recommender/img/data_v3_results.png)

