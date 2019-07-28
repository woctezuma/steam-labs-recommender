import unittest

import download_results
import file_utils


def get_app_id_for_sleeping_dogs():
    # In July 2019, Sleeping Dogs is my 51st most played game. So it does not appear on the web page of the recommender.
    app_id_for_sleeping_dogs = 202170

    return app_id_for_sleeping_dogs


class TestDownloadResultsMethods(unittest.TestCase):

    def test_exclusion_of_a_game_outside_of_the_top_50(self):

        ignored_app_ids = file_utils.load_input_app_ids()

        result_A = download_results.download_recommender_results(ignored_app_ids=ignored_app_ids)

        ignored_app_ids = file_utils.load_input_app_ids()
        if get_app_id_for_sleeping_dogs() in ignored_app_ids:
            raise AssertionError()
        ignored_app_ids.append(get_app_id_for_sleeping_dogs())

        result_B = download_results.download_recommender_results(ignored_app_ids=ignored_app_ids)

        for (a, b) in zip(result_A['recommendations'], result_B['recommendations']):
            if a['app_ids'] != b['app_ids']:
                print('Results differ: exclusion of the top 50 games vs. exclusion of the top 51 games.')
                print(a['algorithm_options'])
                print(b['algorithm_options'])
                print()

        return


if __name__ == '__main__':
    unittest.main()
