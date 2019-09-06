from inverse_problem import aggregate_recommendations, count_occurrences, summarize_occurrences
from inverse_problem import get_popularity_bias_denominator, get_popularity_bias_range, get_release_recency_bias_range


def identify_common_bias(bias_val,
                         bias_occurrences):
    n = max(bias_occurrences)
    indices = [ind for ind in range(len(bias_occurrences)) if bias_occurrences[ind] == n]
    bias_argmax_list = [bias_val[ind] for ind in indices]

    return bias_argmax_list, n


def extract_data_with_equal_release_recency_bias(app_id,
                                                 aggregated_recommendations,
                                                 rb_occurrences_dict,
                                                 verbose=False):
    rb_argmax_list, n = identify_common_bias(get_release_recency_bias_range(),
                                             rb_occurrences_dict[str(app_id)])

    data = dict()

    for rb_argmax in rb_argmax_list:
        if verbose:
            print('\nAppID = {}'.format(app_id))
            print('Extracting data with release recency bias equal to {} months.'.format(rb_argmax))

        X = []
        y = []

        for elem in aggregated_recommendations[str(app_id)]:
            if elem['release_bias'] == rb_argmax:
                x_i = elem['popularity_bias'] / get_popularity_bias_denominator()
                y_i = elem['tweaked_score']

                X.append(x_i)
                y.append(y_i)

        if verbose:
            print('X = {}'.format(X))
            print('y = {}'.format(y))

        if len(y) != n:
            raise AssertionError()

        data[str(rb_argmax)] = dict(X=X,
                                    y=y)

    return data


def extract_data_with_equal_popularity_bias(app_id,
                                            aggregated_recommendations,
                                            pb_occurrences_dict,
                                            verbose=False):
    pb_argmax_list, n = identify_common_bias(get_popularity_bias_range(),
                                             pb_occurrences_dict[str(app_id)])

    data = dict()

    for pb_argmax in pb_argmax_list:
        if verbose:
            print('\nAppID = {}'.format(app_id))
            print('Extracting data with popularity bias equal to {}/{}.'.format(pb_argmax,
                                                                                get_popularity_bias_denominator()))

        X = []
        y = []

        for elem in aggregated_recommendations[str(app_id)]:
            if elem['popularity_bias'] == pb_argmax:
                x_i = elem['release_bias']
                y_i = elem['tweaked_score']

                X.append(x_i)
                y.append(y_i)

        if verbose:
            print('X = {}'.format(X))
            print('y = {}'.format(y))

        if len(y) != n:
            raise AssertionError()

        data[str(pb_argmax)] = dict(X=X,
                                    y=y)

    return data


def extract_data(app_id,
                 aggregated_recommendations,
                 verbose=False):
    if verbose:
        print('\nAppID = {}'.format(app_id))
        print('Extracting all available data.')

    X = []
    y = []

    for elem in aggregated_recommendations[str(app_id)]:
        x_i = [
            elem['popularity_bias'] / get_popularity_bias_denominator(),
            elem['release_bias']
        ]
        y_i = elem['tweaked_score']

        X.append(x_i)
        y.append(y_i)

    if verbose:
        print('X = {}'.format(X))
        print('y = {}'.format(y))

    data = dict(X=X,
                y=y)

    return data


def main():
    aggregated_recommendations = aggregate_recommendations(verbose=False)

    stats = count_occurrences(aggregated_recommendations,
                              verbose=False)

    app_ids, pb_occurrences_dict, rb_occurrences_dict = summarize_occurrences(aggregated_recommendations,
                                                                              stats,
                                                                              chosen_num_occurrences=max(stats.keys()),
                                                                              verbose=True)

    for app_id in app_ids:
        data = extract_data_with_equal_release_recency_bias(app_id,
                                                            aggregated_recommendations,
                                                            rb_occurrences_dict,
                                                            verbose=True)
        data = extract_data_with_equal_popularity_bias(app_id,
                                                       aggregated_recommendations,
                                                       pb_occurrences_dict,
                                                       verbose=True)
        data = extract_data(app_id,
                            aggregated_recommendations,
                            verbose=True)

    return


if __name__ == '__main__':
    main()
