import requests
import os
from scrapers.spareroom_scrape import spareroom_scraper
from scrapers.rightmove_scrape import rightmove_scraper
from connection import check_and_insert_db
from discord_post import post_on_discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")

urls = {
    "rightmove": "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=USERDEFINEDAREA%5E%7B%22polylines%22%3A%22_%60tyHbvPwiBcwMboDukUhoFhRfnGrpMioCh~QssLp_B%22%7D&maxBedrooms=1&minBedrooms=0&maxPrice=1500&propertyTypes=&mustHave=&dontShow=&furnishTypes=furnished&keywords=",
    "spareroom": "https://www.spareroom.co.uk/flatshare/index.cgi?&search_id=1274474201&offset=10&sort_by=days_since_placed",
}

# Add to not get fetch errors for some websites
headers = requests.utils.default_headers()
headers.update(
    {
        "User-Agent": "User Agent 1.0",
    }
)

for site, url in urls.items():
    page = requests.get(url, headers=headers)
    match site:
        case "rightmove":
            scraped_props = rightmove_scraper(page)
            new_properties = check_and_insert_db(scraped_props, site)
            post_on_discord(new_properties, TOKEN, 1198606867514015825)
        case "spareroom":
            scraped_props = spareroom_scraper(page)
            new_properties = check_and_insert_db(scraped_props, site)
            post_on_discord(new_properties, TOKEN, 1009529852728197274)
