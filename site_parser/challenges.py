import requests
import logging
from bs4 import BeautifulSoup, Tag as bsTag


class EmptyResultException(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def get_page_with_challenges(url="https://www.codewars.com/kata/search/python", query_params=None) -> str | None:
    """
    Function requests html page of challenges' search from CodeWars

    :param url: challenges search url
    :param query_params: dict of parameters for search, e.g. beta=false, page=1, etc.
    :return: str - text of response
    """
    if query_params is None:
        query_params = {'beta': 'false'}

    response = requests.get(url, params=query_params)
    response.raise_for_status()

    return response.text


def extract_divs_with_challenges(page: str) -> list[bsTag]:
    """
    Function parses response page with bs4 and returns list of divs with katas

    :param page:
    :return: list[bsTag] - list of div tags with katas' information
    """

    try:
        if not page:
            raise EmptyResultException("Returned from API page is empty")

        bs = BeautifulSoup(page, 'html.parser')
        kata_divs: list[bsTag] = bs.find_all("div", class_="list-item-kata")
        if len(kata_divs) == 0:
            raise EmptyResultException("No div elements with kata data were found on parsed page")


        return kata_divs

    except EmptyResultException as err:
        logging.error(err)


def get_challenges(page_limit=None) -> list[dict]:
    """
    Function iterates through all pages and returns list of challenges

    :param page_limit: (optional) sets limit of pages for parsing
    :return: list[dict] - [{id:123, name: 'math-test'}, ...]
    """

    challenges = []
    page_number = 0
    while True:
        try:
            page_number += 1
            search_page = get_page_with_challenges(query_params={'beta': 'false', 'page': page_number})
            kata_divs = extract_divs_with_challenges(search_page)
            for div in kata_divs:
                challenges.append({"id": div['id'], "name": div['data-title']})
            if page_limit is not None and page_number == page_limit:
                logging.info(f"Predefined limit of pages is reached: {page_limit}")
                break
        except requests.HTTPError as http_err:
            if page_number > 1:
                logging.info(f"Limit of pages is reached: {page_number}")
            else:
                logging.error(f"HTTP error occurred: {http_err}")
            break
        except Exception as err:
            logging.error(f"Other request error occurred: {err}")
            break

    try:
        if len(challenges) == 0:
            raise EmptyResultException("challenges list is empty!")
    except EmptyResultException as err:
        logging.error(err)

    return challenges
