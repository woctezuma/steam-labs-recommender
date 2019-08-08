from personal_info import get_cookie_dict


def get_data_path():
    data_path = "data_v3/"

    return data_path


def get_input_file_name():
    input_file_name = get_data_path() + "inputs.json"

    return input_file_name


def get_result_file_name():
    result_file_name = get_data_path() + "results.json"

    return result_file_name


def get_steam_id():
    steam_id = '76561198028705366'

    return steam_id


def get_session_id():
    cookies = get_cookie_dict()

    session_id = cookies['sessionid']

    return session_id


def get_recommender_url(steam_id=None):
    if steam_id is None:
        steam_id = get_steam_id()

    recommender_url = "https://store.steampowered.com/recommender/" + steam_id + "/"

    return recommender_url


def main():
    recommender_url = get_recommender_url()

    return


if __name__ == '__main__':
    main()
