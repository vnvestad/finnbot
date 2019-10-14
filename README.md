# finnbot
Bot crawler for scraping data from finn.no

# Deploy
```
scrapyd-deploy
```

# Start and stop
```
curl http://localhost:6800/schedule.json -d project=finnbot -d spider=finn
```