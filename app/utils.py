"""
Helper functions for our app, like
"""


def slugify(name):
    """
    Transforms a title to a slug.

    Since we use Python 3, unicode is on the table.

    :param: a string
    :return: a string
    """
    slug = name.lower().replace(" ", "-")
    return slug