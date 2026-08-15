import httpx


class CodeforcesClient:
    BASE_URL = "https://codeforces.com/api"

    def __init__(self):
        self.client = httpx.Client()

    def get_user(self, handle: str) -> dict:
        response = self.client.get(
            f"{self.BASE_URL}/user.info",
            params={"handles": handle},
        )

        response.raise_for_status()

        data = response.json()

        if data["status"] != "OK":
            raise RuntimeError(data.get("comment", "Codeforces API request failed"))

        return data["result"][0]
