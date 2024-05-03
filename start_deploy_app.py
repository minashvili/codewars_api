from site_parser import challenges
from create_and_filling_db import data_to_database


data_to_database.work_with_db(challenges.get_challenges())

