import json

from download_inputs import download_recommender_inputs
from download_results import download_recommender_results
from utils import get_input_file_name, get_result_file_name


def load_inputs():
    with open(get_input_file_name(), 'r') as f:
        data = json.load(f)

    return data


def load_results():
    with open(get_result_file_name(), 'r') as f:
        data = json.load(f)

    return data


def update_inputs():
    data = download_recommender_inputs()

    if data is not None:
        print('Saving inputs to disk.')
        with open(get_input_file_name(), 'w') as f:
            json.dump(data, f)

    return data


def update_results(ignored_app_ids=None):
    data = download_recommender_results(ignored_app_ids=ignored_app_ids)

    if data is not None:
        print('Saving results to disk.')
        with open(get_result_file_name(), 'w') as f:
            json.dump(data, f)

    return data


def load_input_app_ids():
    data = load_inputs()

    input_app_ids = [d["a"] for d in data]

    return input_app_ids


def load_app_info():
    data = load_results()

    app_info = data['app_info']

    return app_info


def load_recommendations():
    data = load_results()

    recommendations = data['recommendations']

    return recommendations


def load_tags():
    data = load_results()

    tags = data['tags']

    return tags


def main(update_json_data=False):
    if update_json_data:
        data = update_inputs()
        data = update_results()

    inputs = load_inputs()
    results = load_results()
    input_app_ids = load_input_app_ids()
    app_info = load_app_info()
    recommendations = load_recommendations()
    tags = load_tags()

    print('#tags = {}'.format(len(tags)))

    return


if __name__ == '__main__':
    main()
