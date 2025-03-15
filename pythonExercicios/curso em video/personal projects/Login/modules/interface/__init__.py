Color = {"": "\033[0m",
         "error": "\033[38;2;255;50;50m",
         "red": "\033[31m",
         "green": "\033[32m",
         "yellow": "\033[33m"}


def down(size=30):
    print('\n' * size)


def line(size=42):
    return '=' * size