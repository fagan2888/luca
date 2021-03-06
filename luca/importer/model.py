"""Models that importers can use for representing financial data."""

class Balance(object):
    """An assertion of an account's balance at a point in time."""

    __slots__ = [
        'sort_key',
        'account',
        'date',
        'amount',
        ]

    event_type = 'balance'

    def __repr__(self):
        return '<%s %r %s %s>' % (type(self).__name__, self.account,
                                  self.date, self.amount)

class Transaction(object):
    """A record stating that that money moved in or out of an account."""

    __slots__ = [
        'sort_key',
        'account',
        'category',  # TODO: remove
        'date',
        'posting_date',
        'description',
        'amount',
        'full_text',
        ]

    event_type = 'transaction'

    def __init__(self):
        self.sort_key = 0
        self.category = None


    def set_full_text(self):
        self.full_text = '{}  {}  {}  {:,}{}'.format(
            self.date.strftime('%Y-%m-%d'),
            self.description,
            self.account,
            abs(self.amount),
            '-' if self.amount < 0 else '')


def can_import_texts_containing(*substrings):
    def annotate(importer):
        def does_this_match(text):
            return all((substring in text) for substring in substrings)
        importer.does_this_match = does_this_match
        return importer
    return annotate
