from personal_info import get_cookie_dict


def get_data_path():
    return "data_v3/"


def get_tag_file_name():
    return get_data_path() + "tags.json"


def get_input_file_name():
    return get_data_path() + "inputs.json"


def get_result_file_name():
    return get_data_path() + "results.json"


def get_steam_id():
    return '76561198028705366'


def get_session_id():
    cookies = get_cookie_dict()

    return cookies['sessionid']


def get_recommender_url(steam_id=None):
    if steam_id is None:
        steam_id = get_steam_id()

    return "https://store.steampowered.com/recommender/" + steam_id + "/"


def main():
    recommender_url = get_recommender_url()

    return


if __name__ == '__main__':
    main()
