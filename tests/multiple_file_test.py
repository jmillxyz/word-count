from indexer.indexer import index


def test_alice_and_sabotage():
    assert index( 'tests/alice.txt', 'tests/sabotage.txt') == {
        'a': 992, 'it': 715, 'and': 1295, 'i': 548, 'in': 657, 'of': 1013,
        'she': 553, 'the': 2465, 'to': 1113, 'you': 642 }
