from test_fixtures import countries


def get_first(iterable, value=None, key=None, default=None):
    match value is None, callable(key):
        case (True, True):
            gen = (val for val in iterable if key(val))
        case (False, True):
            gen = (val for val in iterable if key(val) == value)
        case (True, False):
            gen = (val for val in iterable if val)
        case (False, False):
            gen = (val for val in iterable if val == value)

    return next(gen, default)


if __name__ == "__main__":
    target_match = {"country": "Norway", "population": 5311916}
    print(get_first(countries, target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(get_first(countries, key=match_scotland))