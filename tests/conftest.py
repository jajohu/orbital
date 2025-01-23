import pytest
import responses


@pytest.fixture
def mock_report_api():
    with responses.RequestsMock() as rsps:
        def setup_response(cost: float, report_id: int):
            rsps.add(
                responses.GET,
                f"https://owpublic.blob.core.windows.net/tech-task/reports/{report_id}",
                json={"id": report_id, "name": "test report name", "credit_cost": cost}
            )
        yield setup_response
