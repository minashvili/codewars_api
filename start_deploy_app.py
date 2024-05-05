from site_parser import challenges
from create_and_filling_db import data_to_database
import logging

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ"
)
data_to_database.work_with_db(challenges.get_challenges())
