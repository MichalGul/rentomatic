# remember fixtures defined in conftest files are automatically imported and globaly avaliable
import pytest
from manage import read_json_configuration
from application.app import create_app

@pytest.fixture
def app():
    app = create_app("testing")
    return app

# Add custom --integration option to pytest command line:
# eg usage pytest -svv --integration
def pytest_addoption(parser):
    parser.addoption("--integration", action="store_true", help="run integration tests")


# Check check test for integration mark and skip if not command run with --integraion flag
def pytest_runtest_setup(item):
    if "integration" in item.keywords and not item.config.getoption("--integration"):
        pytest.skip("need --integration option to run")

@pytest.fixture(scope="session")
def app_configuration():
    return read_json_configuration("testing")
