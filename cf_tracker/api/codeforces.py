import httpx


class CodeforcesClient:
    BASE_URL = "https://codeforces.com/api"

    def __init__(self, client=None):
        if client is None:
            client = httpx.Client()

        self.client = client

    def get_user(self, handle: str) -> dict:
        response = self.client.get(
            f"{self.BASE_URL}/user.info",
            params={"handles": handle},
        )

        response.raise_for_status()

        data = response.json()

        if data["status"] != "OK":
            raise RuntimeError(
                data.get("comment", "Codeforces API request failed")
            )

        return data["result"][0]

    def get_submissions(
        self,
        handle: str,
        from_: int = 1,
        count: int = 100,
    ) -> list[dict]:
        response = self.client.get(
            f"{self.BASE_URL}/user.status",
            params={
                "handle": handle,
                "from": from_,
                "count": count,
            },
        )

        response.raise_for_status()

        data = response.json()

        if data["status"] != "OK":
            raise RuntimeError(
                data.get("comment", "Codeforces API request failed")
            )

        return data["result"]
