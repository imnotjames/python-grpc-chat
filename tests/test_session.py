from chat.session import Memory


def test_memory_initializes():
    memory = Memory()
    memory.initialize('foo', 'bar')

    assert memory.has('foo')
    assert not memory.has('bar')
    assert memory.get_username('foo') == 'bar'


def test_memory_delete():
    memory = Memory()
    memory.initialize('foo', 'bar')
    memory.delete('foo')

    assert not memory.has('foo')


def test_memory_unread():
    memory = Memory()
    memory.initialize('foo', 'bar')

    memory.append_unread_message('foo', 1)
    memory.append_unread_message('foo', 2)
    memory.append_unread_message('foo', 3)

    a, b, c = memory.pop_unread_messages('foo')

    assert a == 1
    assert b == 2
    assert c == 3


def test_memory_unread_limits():
    memory = Memory()
    memory.initialize('foo', 'bar')

    for i in range(5000):
        memory.append_unread_message('foo', i)

    count_unread = 0

    for m in memory.pop_unread_messages('foo'):
        count_unread += 1

    assert count_unread == 50