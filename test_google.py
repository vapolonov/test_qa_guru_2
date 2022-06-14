import pytest


@pytest.fixture()
def before_each():
    print('Called before each test')


@pytest.fixture(scope='session', autouse=True)
def before_all(request):
    print('Called before all tests' + request.node.name)


def test_first(before_each):
    pass


def test_second(before_each):
    assert 1 == 2, 'Единица не должна быть равна двойке!'

