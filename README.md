# README File
Project that looks to scrape property websites and send notifications to discord for the users to see, this program only runs once.

Recommend setting up crontab to execute on a cycle:
```
*/5 * * * * /bin/python /property-scraper/main.py >> /property-scraper/output.log
```

## Environment Variables
Supply 3 environment variables to enable the program to function:
- DB_USER
- DB_PASS
- DISCORD_TOKEN