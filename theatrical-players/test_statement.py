import pytest
from statement import statement


@pytest.fixture
def plays():
    return {
        "hamlet": {"type": "tragedy", "name": "Hamlet"},
        "pies": {"type": "comedy", "name": "Lord of Pies"},
        "foobar": {"type": "neither", "name": "FooBar"},
    }


@pytest.fixture
def invoice():
    def _make_invoice(playID, audience):
        return {
            "customer": "BigCo",
            "performances": [{"playID": playID, "audience": audience}],
        }

    return _make_invoice


def test_statement_for_two_plays(invoice, plays):
    inv = invoice("hamlet", 1)
    inv["performances"].append({"playID": "pies", "audience": 1})
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Hamlet: $400.00 (1 seats)
 Lord of Pies: $303.00 (1 seats)
Amount owed is $703.00
You earned 0 credits
"""
    )
