import csv
from datetime import datetime
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }
        self.current_url = ""
        self.soup = None
        self.scraped_data = {}

    def fetch_page(self, url):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        try:
            print(f"\nConnecting to {url}...")
            response = requests.get(
                url,
                headers=self.headers,
                timeout=12
            )
            response.raise_for_status()
            self.current_url = url
            self.soup = BeautifulSoup(response.text, "html.parser")
            print("Page fetched successfully!")
            return True
        except requests.exceptions.HTTPError as error:
            print(f"HTTP Error: {error}")
        except requests.exceptions.ConnectionError:
            print("Connection Error. Check your internet or URL.")
        except requests.exceptions.Timeout:
            print("Timeout Error. Server took too long to respond.")
        except requests.exceptions.RequestException as error:
            print(f"Request Error: {error}")
        return False

    def scrape_summary(self):
        if not self.soup:
            return
        title = (
            self.soup.title.string.strip()
            if self.soup.title
            else "No title available"
        )
        meta_desc = "No meta description found"
        desc_tag = (
            self.soup.find("meta", attrs={"name": "description"})
            or self.soup.find(
                "meta",
                attrs={"property": "og:description"}
            )
        )
        if desc_tag and desc_tag.get("content"):
            meta_desc = desc_tag["content"].strip()
        h1_count = len(self.soup.find_all("h1"))
        h2_count = len(self.soup.find_all("h2"))
        h3_count = len(self.soup.find_all("h3"))
        p_count = len(self.soup.find_all("p"))
        link_count = len(self.soup.find_all("a"))
        img_count = len(self.soup.find_all("img"))
        print("\n" + "=" * 60)
        print("PAGE OVERVIEW")
        print("=" * 60)
        print(f"URL          : {self.current_url}")
        print(f"Page Title   : {title}")
        print(f"Description  : {meta_desc[:120]}")
        print("-" * 60)
        print(f"H1 Tags      : {h1_count}")
        print(f"H2 Tags      : {h2_count}")
        print(f"H3 Tags      : {h3_count}")
        print(f"Paragraphs   : {p_count}")
        print(f"Hyperlinks   : {link_count}")
        print(f"Images       : {img_count}")
        print("=" * 60)

    def scrape_headings(self):
        if not self.soup:
            return
        headings = []
        for tag in self.soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headings.append({
                    "tag": tag.name.upper(),
                    "text": text
                })
        print("\n" + "=" * 60)
        print("EXTRACTED HEADINGS")
        print("=" * 60)
        if not headings:
            print("No headings found.")
            return
        for index, item in enumerate(headings, start=1):
            print(
                f"[{item['tag']}] "
                f"{index:02d}. {item['text']}"
            )

        self.scraped_data["headings"] = headings

    def scrape_links(self, limit=25):

        if not self.soup:
            return

        links = []

        for a_tag in self.soup.find_all("a", href=True):

            href = a_tag["href"].strip()

            text = (
                a_tag.get_text(strip=True)
                or "[No Anchor Text]"
            )

            full_url = urljoin(self.current_url, href)

            if (
                href
                and not href.startswith("javascript:")
                and not href.startswith("#")
            ):
                links.append({
                    "text": text,
                    "url": full_url
                })

        print("\n" + "=" * 60)
        print("EXTRACTED LINKS")
        print("=" * 60)

        if not links:
            print("No hyperlinks found.")
            return

        for index, link in enumerate(links[:limit], start=1):
            print(
                f"{index:02d}. "
                f"{link['text'][:30]:<32} -> "
                f"{link['url']}"
            )

        self.scraped_data["links"] = links

    def scrape_paragraphs(self, limit=10):

        if not self.soup:
            return

        paragraphs = [
            p.get_text(strip=True)
            for p in self.soup.find_all("p")
            if len(p.get_text(strip=True)) > 20
        ]

        print("\n" + "=" * 60)
        print("EXTRACTED PARAGRAPHS")
        print("=" * 60)

        if not paragraphs:
            print("No meaningful paragraphs found.")
            return

        for index, text in enumerate(
            paragraphs[:limit],
            start=1
        ):
            print(f"\nParagraph {index}:\n{text}")

        self.scraped_data["paragraphs"] = paragraphs

    def scrape_images(self, limit=15):

        if not self.soup:
            return

        images = []

        for img in self.soup.find_all("img"):

            src = img.get("src") or img.get("data-src")
            alt = img.get("alt", "No Alt Text").strip()

            if src:
                images.append({
                    "alt": alt,
                    "src": urljoin(self.current_url, src)
                })

        print("\n" + "=" * 60)
        print("EXTRACTED IMAGES")
        print("=" * 60)

        if not images:
            print("No images found.")
            return

        for index, img in enumerate(
            images[:limit],
            start=1
        ):
            print(
                f"{index:02d}. "
                f"Alt: {img['alt'][:25]:<26} | "
                f"URL: {img['src']}"
            )

        self.scraped_data["images"] = images

    def export_data(self):

        if not self.scraped_data:
            print("\nNo data available to export.")
            return

        domain = urlparse(
            self.current_url
        ).netloc.replace(".", "_")

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        if "headings" in self.scraped_data:

            file_name = (
                f"scraped_headings_"
                f"{domain}_{timestamp}.csv"
            )

            with open(
                file_name,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Tag",
                    "Heading Text"
                ])

                for item in self.scraped_data["headings"]:
                    writer.writerow([
                        item["tag"],
                        item["text"]
                    ])

            print(f"Headings saved to: {file_name}")

        if "links" in self.scraped_data:

            file_name = (
                f"scraped_links_"
                f"{domain}_{timestamp}.csv"
            )

            with open(
                file_name,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Anchor Text",
                    "Target URL"
                ])

                for item in self.scraped_data["links"]:
                    writer.writerow([
                        item["text"],
                        item["url"]
                    ])

            print(f"Links saved to: {file_name}")


def select_demo_url():

    print("\nSelect a Test Website")
    print("1. Quotes to Scrape")
    print("2. Books to Scrape")
    print("3. Python Wikipedia")
    print("4. Enter Custom URL")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        return "http://quotes.toscrape.com"

    elif choice == "2":
        return "http://books.toscrape.com"

    elif choice == "3":
        return (
            "https://en.wikipedia.org/wiki/"
            "Python_(programming_language)"
        )

    else:
        return input(
            "Enter custom website URL: "
        ).strip()

def main():
    scraper = WebScraper()
    print("\n" + "#" * 50)
    print("        INTERACTIVE WEB SCRAPER")
    print("#" * 50)
    while True:
        print("\n" + "=" * 45)
        print("MAIN MENU")
        print("=" * 45)
        print("1. Load / Change Website URL")
        print("2. View Page Overview")
        print("3. Scrape Headings")
        print("4. Scrape Hyperlinks")
        print("5. Scrape Text Paragraphs")
        print("6. Scrape Image URLs")
        print("7. Run Complete Scan")
        print("8. Export Data to CSV")
        print("9. Exit")
        print("=" * 45)
        choice = input(
            "Enter your choice (1-9): "
        ).strip()
        if choice == "1":
            target_url = select_demo_url()
            if target_url:
                scraper.fetch_page(target_url)
        elif (
            choice in ["2", "3", "4", "5", "6", "7", "8"]
            and not scraper.soup
        ):
            print(
                "\nPlease load a website first "
                "using Option 1."
            )
        elif choice == "2":
            scraper.scrape_summary()
        elif choice == "3":
            scraper.scrape_headings()
        elif choice == "4":
            scraper.scrape_links()
        elif choice == "5":
            scraper.scrape_paragraphs()
        elif choice == "6":
            scraper.scrape_images()
        elif choice == "7":
            scraper.scrape_summary()
            scraper.scrape_headings()
            scraper.scrape_links(limit=15)
            scraper.scrape_paragraphs(limit=5)
            scraper.scrape_images(limit=10)
        elif choice == "8":
            scraper.export_data()
        elif choice == "9":
            print("\nThank you for using Web Scraper!")
            print("Goodbye.\n")
            break
        else:
            print(
                "\nInvalid choice! "
                "Please select a number from 1 to 9."
            )

if __name__ == "__main__":
    main()