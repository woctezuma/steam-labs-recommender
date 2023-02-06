import requests

from personal_info import (
    get_cookie_dict,
    update_and_save_cookie_to_disk_if_values_changed,
)
from utils import get_recommender_url, get_session_id, get_steam_id


def get_recommender_inputs_url(steam_id=None):
    if steam_id is None:
        steam_id = get_steam_id()

    recommender_results_url = get_recommender_url(steam_id) + "inputs"

    return recommender_results_url


def get_recommender_inputs_request_params():
    params = {
        "sessionid": get_session_id(),
        "steamid": get_steam_id(),
    }

    return params


def download_recommender_inputs():
    url = get_recommender_inputs_url()
    params = get_recommender_inputs_request_params()
    cookies = get_cookie_dict()

    response = requests.get(url, params=params, cookies=cookies)

    if response.status_code == 200:
        result = response.json()

        jar = dict(response.cookies)
        update_and_save_cookie_to_disk_if_values_changed(cookies, jar)
    else:
        print(
            'Download of inputs failed with status code {}.'.format(
                response.status_code,
            ),
        )
        result = None

    return result


def main():
    result = download_recommender_inputs()

    return


if __name__ == '__main__':
    main()
