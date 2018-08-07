from chat.authentication import Memory


def test_memory_authentication():
    memory = Memory({'foo': 'bar'})

    assert memory.authenticate('foo', 'bar') == True
    assert memory.authenticate('foo', 'baz') == False
    assert memory.authenticate('foo', 5) == False
    assert memory.authenticate('bar', 'bar') == False