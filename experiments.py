# Objective: compare the recommendations returned in two settings:
# i)  after excluding the top 50 games, as it can be manually done on the recommender website,
# ii) after excluding the top 51 games, which is impossible to manually do.
#
# The reason behind this experiment is that, if the top 50 games are excluded, then the 51st game should be the most
# important one. So, including/excluding the 51st game should have a large impact on the results... if the recommender
# takes it into account.
#
# The conclusion of this experiment is that there is not point in excluding any game outside of the top 50, because
# the recommender system does not seem to take these exclusions into account.

from download_results import download_recommender_results
from file_utils import load_input_app_ids


def get_app_id_for_sleeping_dogs():
    # In July 2019, Sleeping Dogs is my 51st most played game. So it does not appear on the web page of the recommender.
    app_id_for_sleeping_dogs = 202170

    return app_id_for_sleeping_dogs


def test_exclusion_of_a_game_outside_of_the_top_50():
    ignored_app_ids = load_input_app_ids()

    result_A = download_recommender_results(ignored_app_ids=ignored_app_ids)

    ignored_app_ids = load_input_app_ids()
    if get_app_id_for_sleeping_dogs() in ignored_app_ids:
        raise AssertionError()
    ignored_app_ids.append(get_app_id_for_sleeping_dogs())

    result_B = download_recommender_results(ignored_app_ids=ignored_app_ids)

    for a, b in zip(result_A['recommendations'], result_B['recommendations']):
        if a['app_ids'] != b['app_ids']:
            print(
                'Results differ: exclusion of the top 50 games vs. exclusion of the top 51 games.',
            )
            print(a['algorithm_options'])
            print(b['algorithm_options'])
            print()

    return


def main():
    test_exclusion_of_a_game_outside_of_the_top_50()

    return


if __name__ == '__main__':
    main()
