batted_total, not_out, runs_scored = 1014, 162, 48426


def batting_average():
    return runs_scored / (batted_total - not_out)


print(f'Geoffrey Boycott has a batting average of {batting_average():.2f}.')
