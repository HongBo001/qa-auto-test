import pytest
import logging
import sys
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
# @pytest.fixture
# def base_url_2():
#     return "http://goappictest.sfjswl.com"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("test_log.log"),
                        logging.StreamHandler(sys.stdout)])
