# codewars_api
Notification app for forcing of completion of new daily kata from [codewars.com](https://www.codewars.com/).
Currently API of codewars.com doesn't have method for retrieval of id of new Code Challenge.
Here we are trying to create fast API endoint for Telegram bot for asking of users to complete daily kata.

## TODO (API interaction):
- [ ] Receiving of data from API/site
  - [x] Create a function, returning of IDs of challenges (katas);
  - [ ] Add logging on errors;
  - [ ] Currently only 30 challenges are returned per request;
  - [ ] Rework requests' parameters (Level/Resolved/Unresolved, etc.). Write an algorithm for retrieving of new Kata if the checked one on previous step has been already solved, otherwise - return `Name` and `url` of new Kata;
- [ ] Local saving of retrieved data;
  - [ ] Create a function for saving challenges in SQLite DB; 
  - [ ] Create a function for checking of first(?) id from the list of previously retrieved Katas;

## TODO (Fast API):
- [ ] Create Fast API endpoint as wrapper for API interaction;

## TODO (Bot):
- [ ] Choose a way of hosting (dockerized or simple systemd daemon);
- [ ] Create base for Telegram Bot;
- [ ] Level settings: add an ability to set Level for suggested Katas by bot;
- [ ] Kata completion notification: send notification by bot when user from bot's chat completed the Kata;
- [ ] Reminder for users who didn't complete Kata: send a message with tagging of users, who didn't complete daily Kata;

## TODO (How to deploy it)
- [ ] git pull repo https://github.com/minashvili/codewars_api.git
- [ ] create the kata_from_codewars.db (sqlite) and use this to create a table create_table.sql 
- [ ] pip install -r requirements.txt
- [ ] data_from_parser_to_database.py
