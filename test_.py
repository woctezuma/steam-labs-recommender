import unittest

import download_inputs
import download_results
import download_tags
import extract_regression_data
import file_utils
import inverse_problem
import personal_info
import release_recency
import utils


class TestDownloadTagsMethods(unittest.TestCase):
    def test_get_recommender_tags_url(self):
        s = download_tags.get_recommender_tags_url()
        assert len(s) > 0


class TestDownloadInputsMethods(unittest.TestCase):
    def test_get_recommender_inputs_url(self):
        s = download_inputs.get_recommender_inputs_url()
        assert len(s) > 0


class TestDownloadResultsMethods(unittest.TestCase):
    def test_get_recommender_results_url(self):
        s = download_results.get_recommender_results_url()
        assert len(s) > 0


class TestUtilsMethods(unittest.TestCase):
    def test_get_data_path(self):
        s = utils.get_data_path()
        assert len(s) > 0

    def test_get_tag_file_name(self):
        s = utils.get_tag_file_name()
        assert len(s) > 0

    def test_get_input_file_name(self):
        s = utils.get_input_file_name()
        assert len(s) > 0

    def test_get_result_file_name(self):
        s = utils.get_result_file_name()
        assert len(s) > 0

    def test_get_steam_id(self):
        s = utils.get_steam_id()
        assert len(s) > 0

    def test_get_recommender_url(self):
        s = utils.get_recommender_url()
        assert len(s) > 0


class TestPersonalInfoMethods(unittest.TestCase):
    def test_get_steam_cookie_file_name(self):
        s = personal_info.get_steam_cookie_file_name()
        assert len(s) > 0

    def test_load_steam_cookie_from_disk(self):
        cookie = personal_info.load_steam_cookie_from_disk()
        assert len(cookie) in [0, 2]

    def test_save_steam_cookie_to_disk(self):
        is_cookie_to_be_saved = personal_info.save_steam_cookie_to_disk(cookie={})
        assert not is_cookie_to_be_saved

    def test_get_cookie_dict(self):
        cookie = personal_info.get_cookie_dict(verbose=True)
        assert len(cookie) in [0, 2]

    def test_update_cookie_dict(self):
        original_cookie = {"hello": 'world', "bonjour": 'tout le monde'}
        dict_with_new_values = {"hello": 'everyone'}
        cookie = personal_info.update_cookie_dict(
            original_cookie,
            dict_with_new_values,
            verbose=True,
        )
        assert all(
            original_cookie[field] == cookie[field]
            for field in original_cookie
            if field not in dict_with_new_values.keys()
        )
        assert all(
            dict_with_new_values[field] == cookie[field]
            for field in dict_with_new_values
        )

    def test_update_and_save_cookie_to_disk_if_values_changed(self):
        original_cookie = {
            "steamLoginSecure": 'a very secured string',
            "sessionid": 'my current session',
        }
        dict_with_new_values = {"sessionid": 'my new session'}
        cookie = personal_info.update_and_save_cookie_to_disk_if_values_changed(
            original_cookie,
            dict_with_new_values,
            file_name_with_personal_info='temp.txt',
            verbose=True,
        )
        assert all(
            original_cookie[field] == cookie[field]
            for field in original_cookie
            if field not in dict_with_new_values.keys()
        )
        assert all(
            dict_with_new_values[field] == cookie[field]
            for field in dict_with_new_values
        )


class TestFileUtilsMethods(unittest.TestCase):
    def test_load_json_from_disk(self):
        file_name = utils.get_tag_file_name()
        data = file_utils.load_json_from_disk(file_name)
        assert len(data) > 0

    def test_load_inputs(self):
        data = file_utils.load_inputs()
        assert len(data) == 50

    def test_load_results(self):
        data = file_utils.load_results()
        assert len(data) == 2

    def test_load_input_app_ids(self):
        data = file_utils.load_input_app_ids()
        assert len(data) == 50

    def test_load_app_info(self):
        data = file_utils.load_app_info()
        assert len(data) > 0

    def test_load_recommendations(self):
        data = file_utils.load_recommendations()
        assert len(data) == 30

    def test_load_tags(self):
        data = file_utils.load_tags()
        assert len(data) > 0


class TestInverseProblemMethods(unittest.TestCase):
    def test_get_popularity_bias_denominator(self):
        popularity_bias_denominator = inverse_problem.get_popularity_bias_denominator()
        assert popularity_bias_denominator == 3

    def test_get_popularity_bias_range(self):
        popularity_bias_range = inverse_problem.get_popularity_bias_range()
        assert popularity_bias_range == [-1, 0, 1, 2, 3]

    def test_get_release_recency_bias_range(self):
        release_recency_bias_range = inverse_problem.get_release_recency_bias_range()
        assert release_recency_bias_range == [6, 12, 24, 36, 60, 120]

    def test_aggregate_recommendations(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=True,
        )
        assert len(aggregated_recommendations) > 0

    def test_count_rankings(self):
        num_rankings, ranking_size = inverse_problem.count_rankings(verbose=True)
        assert num_rankings == 30
        assert ranking_size == 400

    def test_count_occurrences(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=True,
        )
        stats = inverse_problem.count_occurrences(
            aggregated_recommendations,
            verbose=True,
        )
        assert len(stats) > 0

    def test_get_total_num_apps(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=True,
        )
        stats = inverse_problem.count_occurrences(
            aggregated_recommendations,
            verbose=True,
        )
        total_num_apps = inverse_problem.get_total_num_apps(stats, verbose=True)

        expected_total_num_apps = len(aggregated_recommendations)

        assert total_num_apps == expected_total_num_apps

    def test_get_total_num_occurrences(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=True,
        )
        stats = inverse_problem.count_occurrences(
            aggregated_recommendations,
            verbose=True,
        )
        total_num_occurrences = inverse_problem.get_total_num_occurrences(
            stats,
            verbose=True,
        )

        num_rankings, ranking_size = inverse_problem.count_rankings(verbose=True)
        expected_total_num_occurrences = num_rankings * ranking_size

        assert total_num_occurrences == expected_total_num_occurrences

    def test_summarize_occurrences(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=True,
        )
        (
            app_ids,
            pb_occurrences_dict,
            rb_occurrences_dict,
        ) = inverse_problem.summarize_occurrences(
            aggregated_recommendations,
            verbose=True,
        )

        assert len(app_ids) > 0
        assert len(app_ids) == len(pb_occurrences_dict)
        assert len(app_ids) == len(rb_occurrences_dict)

        pb_val = inverse_problem.get_popularity_bias_range()
        rb_val = inverse_problem.get_release_recency_bias_range()

        assert all(
            len(occurrences) == len(pb_val)
            for occurrences in pb_occurrences_dict.values()
        )
        assert all(
            len(occurrences) == len(rb_val)
            for occurrences in rb_occurrences_dict.values()
        )


class TestReleaseRecencyMethods(unittest.TestCase):
    def test_get_unix_time_stamp(self):
        unix_time_stamp_as_int = release_recency.get_unix_time_stamp()
        assert unix_time_stamp_as_int > 0

    def test_convert_str_to_unix_time_stamp(self):
        unix_time_stamp_as_int = release_recency.convert_str_to_unix_time_stamp(
            date_as_str='2019-07-28',
            date_format='%Y-%m-%d',
        )
        assert unix_time_stamp_as_int > 0

    def test_get_release_recency(self):
        delta_time_stamp = release_recency.get_release_recency(
            app_id=49520,
            reference_date='2019-07-28',
            verbose=True,  # Borderlands 2
        )
        assert delta_time_stamp > 0

    def test_get_hard_coded_reference_date(self):
        date_str = release_recency.get_hard_coded_reference_date()
        assert len(date_str) == 10


class TestExtractRegressionDataMethods(unittest.TestCase):
    def test_identify_common_bias(self):
        bias_val = inverse_problem.get_release_recency_bias_range()
        bias_occurrences = [0, 2, 5, 10, 5, 1]
        expected_argmax_ind = 3  # to match the 10

        assert max(bias_occurrences) == bias_occurrences[expected_argmax_ind]

        bias_argmax_list, n = extract_regression_data.identify_common_bias(
            bias_val,
            bias_occurrences,
        )
        bias_argmax = bias_argmax_list[0]

        assert len(bias_argmax_list) == 1
        assert bias_argmax == bias_val[expected_argmax_ind]
        assert n == bias_occurrences[expected_argmax_ind]

    def test_extract_data_with_equal_release_recency_bias(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=False,
        )

        (
            app_ids,
            pb_occurrences_dict,
            rb_occurrences_dict,
        ) = inverse_problem.summarize_occurrences(
            aggregated_recommendations,
            verbose=False,
        )

        for app_id in app_ids:
            data = extract_regression_data.extract_data_with_equal_release_recency_bias(
                app_id,
                aggregated_recommendations,
                rb_occurrences_dict,
                verbose=True,
            )

            for rb_argmax in data:
                X = data[rb_argmax]['X']
                y = data[rb_argmax]['y']
                assert len(X) == len(y)

    def test_extract_data_with_equal_popularity_bias(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=False,
        )

        (
            app_ids,
            pb_occurrences_dict,
            rb_occurrences_dict,
        ) = inverse_problem.summarize_occurrences(
            aggregated_recommendations,
            verbose=False,
        )

        for app_id in app_ids:
            data = extract_regression_data.extract_data_with_equal_popularity_bias(
                app_id,
                aggregated_recommendations,
                pb_occurrences_dict,
                verbose=True,
            )
            for pb_argmax in data:
                X = data[pb_argmax]['X']
                y = data[pb_argmax]['y']
                assert len(X) == len(y)

    def test_extract_data(self):
        aggregated_recommendations = inverse_problem.aggregate_recommendations(
            verbose=False,
        )

        (
            app_ids,
            pb_occurrences_dict,
            rb_occurrences_dict,
        ) = inverse_problem.summarize_occurrences(
            aggregated_recommendations,
            verbose=False,
        )

        for app_id in app_ids:
            data = extract_regression_data.extract_data(
                app_id,
                aggregated_recommendations,
                verbose=True,
            )

            X = data['X']
            y = data['y']
            assert len(X) == len(y)


if __name__ == '__main__':
    unittest.main()
