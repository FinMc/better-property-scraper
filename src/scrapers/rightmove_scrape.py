from bs4 import BeautifulSoup


def rightmove_scraper(page):
    soup = BeautifulSoup(page.content, "html.parser")
    results = []
    for listing in soup.findAll("div", attrs={"class": "l-searchResult"}):
        id = listing["id"].split("-")[1]
        address = listing.find("address").text.replace("\n", "")
        price = listing.find("span", attrs={"class": "propertyCard-priceValue"}).text
        link = (
            "https://www.rightmove.co.uk"
            + listing.find("div", attrs={"class": "propertyCard-details"}).find("a")[
                "href"
            ]
        )
        name = address.strip()
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
