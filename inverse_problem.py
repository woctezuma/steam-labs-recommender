from file_utils import load_recommendations


def aggregate_recommendations(verbose=True):
    recommendations = load_recommendations()

    aggregated_recommendations = dict()

    denominator = 3

    for ranking in recommendations:

        popularity_bias = int(denominator * float(ranking['algorithm_options']['popularity_bias']))
        release_recency_bias = int(ranking['algorithm_options']['release_recency_bias'])

        for (app_id, score) in zip(ranking['app_ids'], ranking['scores']):
            tweaked_output = float(ranking['score_scale']) * float(score)

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
        print(aggregated_recommendations)

    return aggregated_recommendations


def main():
    aggregated_recommendations = aggregate_recommendations(verbose=True)

    return


if __name__ == '__main__':
    main()
