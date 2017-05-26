import example


def leaky_function(length):
    array = example.get_array_leaky(length)


def safe_function(length):
    array = example.get_array_safe(length)


if __name__ == '__main__':
    length = 1000
    for _ in range(10):
        # leaky_function(length)
        safe_function(length)
