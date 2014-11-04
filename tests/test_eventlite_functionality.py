import eventlite


def test_eventlite_simple():
    objs = []

    def myfunction(foo):
        eventlite.emit(foo)

    def handler(foo):
        objs.append(foo)

    myfunction('one')

    with eventlite.handler(handler):
        myfunction('two')

    myfunction('three')

    with eventlite.handler(handler):
        myfunction('four')

    assert objs == ['two', 'four']
