import requests

from personal_info import get_cookie_dict, update_and_save_cookie_to_disk_if_values_changed
from utils import get_steam_id, get_session_id, get_recommender_url


def get_recommender_tags_url(steam_id=None):
    if steam_id is None:
        steam_id = get_steam_id()

    return get_recommender_url(steam_id) + "tags"


def get_recommender_tags_request_params():
    return dict(
        sessionid=get_session_id(),
    )


def download_recommender_tags():
    url = get_recommender_tags_url()
    params = get_recommender_tags_request_params()
    cookies = get_cookie_dict()

    response = requests.get(url, params=params, cookies=cookies)

    if response.status_code == 200:
        result = response.json()

        jar = dict(response.cookies)
        update_and_save_cookie_to_disk_if_values_changed(cookies, jar)
    else:
        print('Download of tags failed with status code {}.'.format(response.status_code))
        result = None

    return result


def main():
    result = download_recommender_tags()

    return


if __name__ == '__main__':
    main()
