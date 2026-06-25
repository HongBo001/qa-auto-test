import random

import pytest

@pytest.mark.login
def _test_rerun():
    x = random.randint(1, 10)
    assert x >=9