from bs4 import BeautifulSoup


def onthemarket_scraper(page):
    soup = BeautifulSoup(page.content, "html.parser")
    results = []
    for listing in soup.findAll("li", attrs={"class": "otm-PropertyCard"}):
        property_div = listing.find("div", {"itemtype": "https://schema.org/Apartment"})
        id = property_div.get("id", "").replace("result-", "")
        address_span = listing.find("span", {"class": "address"})
        address = address_span.find("a").text.strip()
        price_div = listing.find("div", {"class": "price"})
        price = price_div.text.strip().split("(")[0]
        link = "https://www.onthemarket.com" + listing.find("a")["href"]
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
