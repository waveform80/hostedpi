import pytest

from hostedpi.picloud import *


def test_enumerate_pis(mock_cloud):
    cloud = PiCloud(api_url='http://localhost:8000/',
                    auth_url='http://localhost:8000/login')
    assert cloud.pis == {}
    mock_cloud._instances = {
    }
