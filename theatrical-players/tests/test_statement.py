import json
import os
import pytest

from statement import statement

def _here(filename):
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, filename)


def test_example_statement():
    with open(_here("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(_here("plays.json")) as f:
        plays = json.loads(f.read())
    assert statement(invoice, plays) == """Statement for BigCo
 Hamlet: $650.00 (55 seats)
 As You Like It: $580.00 (35 seats)
 Othello: $500.00 (40 seats)
Amount owed is $1,730.00
You earned 47 credits
""" 

