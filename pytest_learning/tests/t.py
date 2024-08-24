import pytest
import tempfile

class C:
    def f(self):
        return 1
    
    def g(self):
        return 2


@pytest.fixture
def c_instance(temporary_dir):
    return C()


@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

# Autouse - Applies the fixture to tests below
# Scope - Scope of fixture (function, class, module, package, session)
@pytest.fixture(autouse=True, scope='module')
def setup_teardown():
    print('setup')
    yield
    print('teardown')


@pytest.fixture(name='fix')
def thisishowyourenameafixture():
    return 5


@pytest.fixture(params=(1, 2, 3, 4))
def an_int(request):
    yield request.param + 2


def test_an_int(an_int):
    print(f'got {an_int=}')


def test_with_new_name(fix):
    print(f'in test {fix=}')


def test_with_setup_teardown(setup_teardown):
    print('in test')


def test_f(c_instance, temporary_dir):
    assert c_instance.f() == 1
    print(temporary_dir)


@pytest.mark.usefixtures('setup_teardown')
def test_g(c_instance):
    assert c_instance.g() == 2


class TestMyThing:
    @pytest.fixture
    def fix(self):
        yield 10
    
    
    def test_1(self, fix):
        print(f'got {fix=}')