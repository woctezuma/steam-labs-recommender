import unittest

import download_inputs
import download_results
import file_utils
import personal_info
import utils


class TestDownloadInputsMethods(unittest.TestCase):

    def test_get_recommender_inputs_url(self):
        s = download_inputs.get_recommender_inputs_url()
        self.assertGreater(len(s), 0)


class TestDownloadResultsMethods(unittest.TestCase):

    def test_get_recommender_results_url(self):
        s = download_results.get_recommender_results_url()
        self.assertGreater(len(s), 0)


class TestUtilsMethods(unittest.TestCase):

    def test_get_data_path(self):
        s = utils.get_data_path()
        self.assertGreater(len(s), 0)

    def test_get_input_file_name(self):
        s = utils.get_input_file_name()
        self.assertGreater(len(s), 0)

    def test_get_result_file_name(self):
        s = utils.get_result_file_name()
        self.assertGreater(len(s), 0)

    def test_get_steam_id(self):
        s = utils.get_steam_id()
        self.assertGreater(len(s), 0)

    def test_get_recommender_url(self):
        s = utils.get_recommender_url()
        self.assertGreater(len(s), 0)


class TestPersonalInfoMethods(unittest.TestCase):

    def test_get_steam_cookie_file_name(self):
        s = personal_info.get_steam_cookie_file_name()
        self.assertGreater(len(s), 0)

    def test_load_steam_cookie_from_disk(self):
        cookie = personal_info.load_steam_cookie_from_disk()
        self.assertIn(len(cookie), [0, 2])

    def test_save_steam_cookie_to_disk(self):
        is_cookie_to_be_saved = personal_info.save_steam_cookie_to_disk(cookie=dict())
        self.assertFalse(is_cookie_to_be_saved)

    def test_get_cookie_dict(self):
        cookie = personal_info.get_cookie_dict(verbose=True)
        self.assertIn(len(cookie), [0, 2])

    def test_update_cookie_dict(self):
        original_cookie = dict(hello='world',
                               bonjour='tout le monde')
        dict_with_new_values = dict(hello='everyone')
        cookie = personal_info.update_cookie_dict(original_cookie,
                                                  dict_with_new_values,
                                                  verbose=True)
        self.assertTrue(all(original_cookie[field] == cookie[field] for field in original_cookie.keys()
                            if field not in dict_with_new_values.keys()))
        self.assertTrue(all(dict_with_new_values[field] == cookie[field] for field in dict_with_new_values.keys()))

    def test_update_and_save_cookie_to_disk_if_values_changed(self):
        original_cookie = dict(steamLoginSecure='a very secured string',
                               sessionid='my current session')
        dict_with_new_values = dict(sessionid='my new session')
        cookie = personal_info.update_and_save_cookie_to_disk_if_values_changed(original_cookie,
                                                                                dict_with_new_values,
                                                                                file_name_with_personal_info='temp.txt',
                                                                                verbose=True)
        self.assertTrue(all(original_cookie[field] == cookie[field] for field in original_cookie.keys()
                            if field not in dict_with_new_values.keys()))
        self.assertTrue(all(dict_with_new_values[field] == cookie[field] for field in dict_with_new_values.keys()))


class TestFileUtilsMethods(unittest.TestCase):

    def test_load_inputs(self):
        data = file_utils.load_inputs()
        self.assertEqual(len(data), 50)

    def test_load_results(self):
        data = file_utils.load_results()
        self.assertEqual(len(data), 3)

    def test_load_input_app_ids(self):
        data = file_utils.load_input_app_ids()
        self.assertEqual(len(data), 50)

    def test_load_app_info(self):
        data = file_utils.load_app_info()
        self.assertGreater(len(data), 0)

    def test_load_recommendations(self):
        data = file_utils.load_recommendations()
        self.assertEqual(len(data), 30)

    def test_load_tags(self):
        data = file_utils.load_tags()
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
