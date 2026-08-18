import pytest

from cf_tracker.api.codeforces import CodeforcesClient


class FakeResponse:
    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


class FakeClient:
    def __init__(self, response):
        self.response = response
        self.url = None
        self.params = None

    def get(self, url, params):
        self.url = url
        self.params = params
        return self.response


def test_get_user():
    response = FakeResponse(
        {
            "status": "OK",
            "result": [
                {
                    "handle": "FortuneIji",
                }
            ],
        }
    )

    fake_client = FakeClient(response)
    client = CodeforcesClient(fake_client)

    user = client.get_user("FortuneIji")

    assert user["handle"] == "FortuneIji"
    assert fake_client.url == "https://codeforces.com/api/user.info"
    assert fake_client.params == {"handles": "FortuneIji"}


def test_get_user_failed_response():
    response = FakeResponse(
        {
            "status": "FAILED",
            "comment": "User not found",
        }
    )

    fake_client = FakeClient(response)
    client = CodeforcesClient(fake_client)

    with pytest.raises(RuntimeError, match="User not found"):
        client.get_user("UnknownUser")


def test_get_submissions():
    response = FakeResponse(
        {
            "status": "OK",
            "result": [
                {
                    "id": 123,
                    "problem": {
                        "name": "Example Problem",
                    },
                    "verdict": "OK",
                }
            ],
        }
    )

    fake_client = FakeClient(response)
    client = CodeforcesClient(fake_client)

    submissions = client.get_submissions(
        "FortuneIji",
        from_=1,
        count=10,
    )

    assert len(submissions) == 1
    assert submissions[0]["id"] == 123
    assert submissions[0]["problem"]["name"] == "Example Problem"
    assert fake_client.url == "https://codeforces.com/api/user.status"
    assert fake_client.params == {
        "handle": "FortuneIji",
        "from": 1,
        "count": 10,
    }

def test_get_submissions_failed_response():
    response = FakeResponse(
        {
            "status": "FAILED",
            "comment": "Handle not found",
        }
    )

    fake_client = FakeClient(response)
    client = CodeforcesClient(fake_client)

    with pytest.raises(RuntimeError, match="Handle not found"):
        client.get_submissions("UnknownUser")
