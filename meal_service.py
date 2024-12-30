"""main api client"""
from typing import Any, Dict

from httpx import Client, Response


class YisMealClient():
    """yi's api client"""


    def __init__(self, api_token: int = 1, headers: Dict[str, Any] = None) -> None:
        self.api_token = api_token
        self.base_url = f"https://www.themealdb.com/api/json/v1/{self.api_token}"
        self.headers = headers or {
            "x-api-key": "289cd13ef6ad436db1c0acd2c07e4527"
        }

        self.client = Client(http2=True)
        # get, put, post, delete

    def _get(self, endpoint: str, params: Dict[str, str] = None) -> Response:
        """get request"""
        return self.client.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)

    def search_by_name(self, name: str) -> Dict[str, Any]:
        """search for a meal by name"""
        return self._get("/search.php", {"s": name}).json()

    def list_by_first_letter(self, first_letter: str) -> Dict[str, Any]:
        """list meals by first letter"""
        return self._get("/search.php", {"f": first_letter}).json()

    def look_up_by_id(self, id: str) -> Dict[str, Any]:
        """look up a meal by id"""
        return self._get("/lookup.php", {"i": id}).json()

    def look_up_random(self) -> Dict[str, Any]:
        """look up a random meal"""
        return self._get("/random.php").json()


def run_file():
    client = YisMealClient()
    print(client.look_up_random())
    print(client.search_by_name("chicken"))


if __name__ == "__main__":
    run_file()