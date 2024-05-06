from vector import Vector


def test_sanity():
    v = Vector()
    assert v.__class__.__name__ == "Vector"
