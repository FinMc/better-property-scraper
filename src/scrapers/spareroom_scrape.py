from bs4 import BeautifulSoup


def spareroom_scraper(page):
    soup = BeautifulSoup(page.content, "html.parser")
    results = []
    for listing in soup.find("ul", attrs={"class": "listing-results"}).findAll(
        "li", attrs={"class": "listing-result"}
    ):
        id = listing["data-listing-id"]
        area = listing["data-listing-neighbourhood"]
        postcode = listing["data-listing-postcode"]
        address = "{area}, {postcode}".format(area=area, postcode=postcode)
        price = listing.find("strong", attrs={"class": "listingPrice"}).text.split("<")[
            0
        ]
        link = "https://www.spareroom.co.uk" + listing.find("a")["href"]
        name = listing["data-listing-title"]
        results.append(
            {
                "id": id,
                "address": address,
                "price": price,
                "link": link,
                "name": name,
            }
        )
    return results
