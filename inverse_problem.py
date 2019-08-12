from file_utils import load_recommendations


def get_popularity_bias_denominator():
    popularity_bias_denominator = 3

    return popularity_bias_denominator


def get_popularity_bias_range():
    popularity_bias_range = [-1, 0, 1, 2, 3]

    return popularity_bias_range


def get_release_recency_bias_range():
    release_recency_bias_range = [6, 12, 24, 36, 60, 120]

    return release_recency_bias_range


def aggregate_recommendations(recommendations=None,
                              verbose=False):
    if recommendations is None:
        recommendations = load_recommendations()

    aggregated_recommendations = dict()

    for ranking in recommendations:
        settings = ranking['algorithm_options']

        popularity_bias = int(get_popularity_bias_denominator() * float(settings['popularity_bias']))
        release_recency_bias = int(settings['release_recency_bias'])
        score_scale = float(ranking['score_scale'])

        for (app_id, score) in zip(ranking['app_ids'], ranking['scores']):
            tweaked_output = score_scale * score

            current_data = dict(pb=popularity_bias,
                                rb=release_recency_bias,
                                s=tweaked_output)

            try:
                aggregated_recommendations[str(app_id)].append(current_data)
            except KeyError:
                aggregated_recommendations[str(app_id)] = [current_data]

    if verbose:
        print('#recommended apIDs = {}'.format(len(aggregated_recommendations)))

    return aggregated_recommendations


def count_rankings(recommendations=None,
                   verbose=False):
    if recommendations is None:
        recommendations = load_recommendations()

    first_ranking_index = 0

    num_rankings = len(recommendations)
    ranking_size = len(recommendations[first_ranking_index]['app_ids'])

    if verbose:
        print('There are {} rankings of {} apps.'.format(num_rankings,
                                                         ranking_size))

    return num_rankings, ranking_size


def count_occurrences(aggregated_recommendations,
                      verbose=False):
    stats = dict()

    for (app_id, occurrences) in aggregated_recommendations.items():
        num_occurrences = len(occurrences)

        try:
            stats[num_occurrences].append(app_id)
        except KeyError:
            stats[num_occurrences] = [app_id]

    if verbose:
        print('How many apps appear in n rankings?')
        for i in sorted(stats.keys()):
            num_apps = len(stats[i])
            print('[n = {:2} occurrences] {:3} apps.'.format(i, num_apps))

        total_num_apps = get_total_num_apps(stats, verbose=verbose)

        total_num_occurrences = get_total_num_occurrences(stats, verbose=verbose)

    return stats


def get_total_num_apps(stats,
                       verbose=False):
    total_num_apps = sum(len(l) for l in stats.values())

    if verbose:
        print('Total: {:5} apps.'.format(total_num_apps))

    return total_num_apps


def get_total_num_occurrences(stats,
                              verbose=False):
    total_num_occurrences = sum(n * len(l) for (n, l) in stats.items())

    if verbose:
        print('Total: {:5} occurrences.'.format(total_num_occurrences))

    return total_num_occurrences


def summarize_occurrences(aggregated_recommendations,
                          stats=None,
                          chosen_num_occurrences=None,
                          verbose=False):
    if stats is None:
        stats = count_occurrences(aggregated_recommendations, verbose=verbose)

    if chosen_num_occurrences is None:
        chosen_num_occurrences = max(stats.keys())

    app_ids = stats[chosen_num_occurrences]

    pb_val = get_popularity_bias_range()
    rb_val = get_release_recency_bias_range()

    pb_occurrences_dict = dict()
    rb_occurrences_dict = dict()

    for app_id in app_ids:
        if verbose:
            print('AppID = {}'.format(app_id))

        val = aggregated_recommendations[app_id]

        pb_occurrences = [0] * len(pb_val)
        rb_occurrences = [0] * len(rb_val)
        for elem in val:
            pb = elem['pb']
            rb = elem['rb']

            pb_occurrences[pb_val.index(pb)] += 1
            rb_occurrences[rb_val.index(rb)] += 1

        pb_occurrences_dict[app_id] = pb_occurrences
        rb_occurrences_dict[app_id] = rb_occurrences

    if verbose:
        print('AppIDs = {}'.format(app_ids))
        print('popularity bias = {} ; #occurrences = {}'.format(pb_val,
                                                                pb_occurrences_dict))
        print('release recency bias = {} ; #occurrences = {}'.format(rb_val,
                                                                     rb_occurrences_dict))

    return app_ids, pb_occurrences_dict, rb_occurrences_dict


def main():
    aggregated_recommendations = aggregate_recommendations(verbose=True)

    stats = count_occurrences(aggregated_recommendations,
                              verbose=True)

    app_ids, pb_occurrences_dict, rb_occurrences_dict = summarize_occurrences(aggregated_recommendations,
                                                                              stats,
                                                                              chosen_num_occurrences=max(stats.keys()),
                                                                              verbose=True)

    return


if __name__ == '__main__':
    main()
