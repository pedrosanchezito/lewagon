# pylint: disable=missing-docstring
# pylint: disable=fixme
# pylint: disable=unused-argument

RATES = {
    'USDEUR' : 0.85,
    'GBPEUR' : 1.13,
    'CHFEUR' : 0.86
}

# `amount` is a `tuple` like (100, EUR). `currency` is a `string`
def convert(amount, currency):
    k = amount[1] + currency
    return round(amount[0]  * RATES[k], 2) if k in RATES else None
