from hello import more_hello, more_goodbye


def test_more_hello():
    assert "Hello:))" == more_hello()


def test_more_goodbye():
    assert "Bye!!" == more_goodbye()
