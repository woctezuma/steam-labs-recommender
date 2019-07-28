import requests

from personal_info import get_cookie_dict
from utils import get_steam_id, get_session_id, get_recommender_url


def get_recommender_results_url(steam_id=None):
    if steam_id is None:
        steam_id = get_steam_id()

    recommender_results_url = get_recommender_url(steam_id) + "results"

    return recommender_results_url


def get_recommender_results_request_params(ignored_app_ids=None):
    if ignored_app_ids is None:
        ignored_app_ids = []

    params = dict(
        sessionid=get_session_id(),
        steamid=get_steam_id(),
        include_played=0,
        algorithm=0,
        reinference=0,
        model_version=0,
    )

    if len(ignored_app_ids) > 0:
        params["ignored"] = ",".join(str(app_id) for app_id in sorted(ignored_app_ids))

    return params


def download_recommender_results(ignored_app_ids=None):
    if ignored_app_ids is None:
        ignored_app_ids = []

    url = get_recommender_results_url()
    params = get_recommender_results_request_params(ignored_app_ids=ignored_app_ids)
    cookies = get_cookie_dict()

    response = requests.get(url, params=params, cookies=cookies)

    if response.status_code == 200:
        result = response.json()
    else:
        result = None

    return result


def main():
    result = download_recommender_results()

    return


if __name__ == '__main__':
    main()