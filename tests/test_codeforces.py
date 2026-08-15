from cf_tracker.api.codeforces import CodeforcesClient


def test_get_user():
    client = CodeforcesClient()

    user = client.get_user("FortuneIji")

    assert user["handle"] == "FortuneIji"
