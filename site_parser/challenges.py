import requests
from bs4 import BeautifulSoup, Tag


class EmptyResultException(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def get_page_with_challenges(url="https://www.codewars.com/kata/search/python", query_params="beta=false") -> str:
    """
    Function requests html page of challenges' search from CodeWars

    :param url: challenges search url
    :param query_params: beta(?), q=&r[]=-8 - difficulty level (8 kyu)
    :return: str -
    """
    try:
        response = requests.get(url, query_params)
        response.raise_for_status()

        return response.text  # should we check response codes? (or log them)

    except requests.HTTPError as http_err:
        pass
        # todo: Replace by logging
        # print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        pass
        # todo: Replace by logging
        # print(f"Other request error occurred: {err}")


def get_challenges() -> list[dict]:
    """
    Function parses response from site and returns list of code challenges

    :return: list[dict] - [{id:123, name: 'math-test'}, ...]
    """
    search_html_page = get_page_with_challenges()
    try:
        if not search_html_page:
            raise EmptyResultException("Returned from API page is empty")

        bs = BeautifulSoup(search_html_page, 'html.parser')
        kata_divs: list[Tag] = bs.find_all("div", class_="list-item-kata")
        if len(kata_divs) == 0:
            raise EmptyResultException("No div elements with kata data were found on parsed page")

        challenges = []
        for div in kata_divs:
            challenges.append({"id": div['id'], "name": div['data-title']})
        # should we check for emptiness of 'challenges' list?

        return challenges

    except EmptyResultException:
        # todo: Replace by logging
        pass


#print(get_challenges())
