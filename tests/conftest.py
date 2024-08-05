# remember fixtures defined in conftest files are automatically imported and globaly avaliable
import pytest

from application.app import create_app

@pytest.fixture
def app():
    app = create_app("testing")
    return app
