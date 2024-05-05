# codewars_api
Notification app for forcing of completion of new daily kata from [codewars.com](https://www.codewars.com/).
Currently, API of codewars.com doesn't have method for retrieval of id of new Code Challenge.
Here we are trying to create fast API endoint for Telegram bot for asking of users to complete daily kata.

## TODO (API interaction):
- [ ] Receiving of data from API/site
  - [x] Create a function, returning of IDs of challenges (katas);
  - [x] Add logging on errors;
  - [x] Currently only 30 challenges are returned per request; (fixed)
  - [ ] Rework requests' parameters (Level/Resolved/Unresolved, etc.).
- [x] Local saving of retrieved data;
  - [x] Create a function for saving challenges in SQLite DB; 
  ~~- [ ] Create a function for checking of first(?) id from the list of previously retrieved Katas;~~

~~## TODO (Fast API):~~
~~- [ ] Create Fast API endpoint as wrapper for API interaction;~~

## CI/CD
- [ ] Prepare deployment scripts
- [ ] Configure github actions for triggering of "new release" 

## TODO (Bot):
- [x] Choose a way of hosting (dockerized or simple systemd daemon); (systemd is chosen)
- [ ] Create "base" for Telegram Bot;
- [ ] Level settings: add an ability to set Level for suggested Katas by bot;
- [ ] Write an algorithm for retrieving of new Kata if the checked one on previous step has been already solved, otherwise - return `Name` and `url` of new Kata;
- [ ] Kata completion notification: send notification by bot when user from bot's chat completed the Kata;
- [ ] Reminder for users who didn't complete Kata: send a message with tagging of users, who didn't complete daily Kata;

## TODO (How to deploy it)
1. git pull repo https://github.com/minashvili/codewars_api.git
1. create the kata_from_codewars.db (sqlite) and use this to create a table create_table.sql 
1. pip install -r requirements.txt
1. data_from_parser_to_database.py
