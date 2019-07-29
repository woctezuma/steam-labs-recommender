from file_utils import load_recommendations


def get_popularity_bias_denominator():
    popularity_bias_denominator = 3

    return popularity_bias_denominator


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
                aggregated_data = aggregated_recommendations[str(app_id)]
            except KeyError:
                aggregated_data = list()

            aggregated_data.append(current_data)

            aggregated_recommendations[str(app_id)] = aggregated_data

    if verbose:
        print('#recommended apIDs = {}'.format(len(aggregated_recommendations)))

    return aggregated_recommendations


def main():
    aggregated_recommendations = aggregate_recommendations(verbose=True)

    return


if __name__ == '__main__':
    main()
