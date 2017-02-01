from cli import command
from test_utilities import Capturing
from tests.test_utilities import Capturing

def test_square():
    with Capturing() as out:
        result = command.main(['--square', '20'])
    assert int(out[0]) == 400

