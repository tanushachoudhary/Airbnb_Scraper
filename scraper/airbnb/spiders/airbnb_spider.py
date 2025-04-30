import scrapy
import json
import requests

class AirbnbSpider(scrapy.Spider):
    name = "airbnb"

    def __init__(self, location="New York", checkin="2024-05-01", checkout="2024-05-05", guests=2, *args, **kwargs):
        super(AirbnbSpider, self).__init__(*args, **kwargs)
        self.location = location
        self.checkin = checkin
        self.checkout = checkout
        self.guests = guests

    def start_requests(self):
        # Simulating paginated search results (this would be a real URL if Airbnb API or endpoint were used)
        for page in range(1, 3):  # Simulate 2 pages
            url = f"https://www.airbnb.com/s/{self.location}/homes?page={page}&checkin={self.checkin}&checkout={self.checkout}&adults={self.guests}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        mock_listing = {
            "title": "Modern Loft in Downtown",
            "location": self.location,
            "address": "123 Main St, New York, NY",
            "price_per_night": 150,
            "currency": "USD",
            "total_price": 600,
            "image_urls": ["https://example.com/image1.jpg"],
            "ratings": 4.85,
            "description": "A modern loft in the heart of the city.",
            "reviews": 212,
            "amenities": ["WiFi", "Kitchen", "Air Conditioning"],
            "host": {
                "name": "Alice",
                "superhost": True,
                "profile_url": "https://example.com/host"
            },
            "property_type": "Loft"
        }

        # Send to backend via POST
        response = requests.post(
            url="http://localhost:8000/api/add_listing",
            json=mock_listing,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 201:
            self.logger.info("Listing successfully sent to backend.")
        else:
            self.logger.error(f"Failed to send listing. Response: {response.text}")
