import collections

my_counter = collections.Counter()

def log_and_count(*args2, **kwargs2):
    def decorator(func):
        def function_inside(*args, **kwargs):
            if "key" in kwargs2:
                kwargs2["counts"][kwargs2["key"]] = kwargs2["counts"][kwargs2["key"]] + 1
            else:
                kwargs2["counts"][func.__name__] = kwargs2["counts"][func.__name__] + 1
            print("called {} with {} and {}".format(func.__name__, args, kwargs))
        return function_inside
    return decorator


def first_with_given_key(iterable, key = lambda item: item):
    list_of = list()
    iterable_ = iter(iterable)
    while not False:
        try:
            iterator = next(iterable_)
            if key(iterator) not in list_of:
                yield iterator
                list_of.insert(0, key(iterator))
        except StopIteration:
            break
print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))