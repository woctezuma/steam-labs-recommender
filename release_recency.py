import time
from datetime import datetime

from file_utils import load_app_info


def get_unix_time_stamp():
    # Reference: https://stackoverflow.com/a/49362936

    unix_time_stamp = time.time()

    unix_time_stamp_as_int = int(unix_time_stamp)

    return unix_time_stamp_as_int


def convert_str_to_unix_time_stamp(date_as_str,
                                   date_format='%Y-%m-%d'):
    # Reference: https://stackoverflow.com/a/30476450

    utc_time = datetime.strptime(date_as_str, date_format)
    unix_time_stamp = (utc_time - datetime(1970, 1, 1)).total_seconds()

    unix_time_stamp_as_int = int(unix_time_stamp)

    return unix_time_stamp_as_int


def get_release_recency(app_id,
                        reference_date=None,
                        app_info=None,
                        verbose=False):
    if app_info is None:
        app_info = load_app_info()

    if reference_date is None:
        reference_time_stamp = get_unix_time_stamp()
    else:
        try:
            if len(reference_date) == 0:
                reference_time_stamp = get_unix_time_stamp()
            else:
                reference_time_stamp = convert_str_to_unix_time_stamp(reference_date)
        except TypeError:
            # reference_date is not a str, so we assume it is already an integer which encodes the Unix time-stamp.
            reference_time_stamp = int(reference_date)

    release_date = app_info[str(app_id)]['r']

    release_recency = (reference_time_stamp - release_date)

    if verbose:
        app_name = app_info[str(app_id)]['n']
        print('{} ({}): {} seconds between release date and reference date.'.format(app_name, app_id, release_recency))

    return release_recency


def main():
    app_info = load_app_info()

    release_recency = get_release_recency(app_id=49520,  # Borderlands 2
                                          reference_date='2019-08-08',  # Date on which results.json was last downloaded
                                          app_info=app_info,
                                          verbose=True)

    return


if __name__ == '__main__':
    main()
