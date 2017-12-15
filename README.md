# Fresh Finder: A map of farmers markets

This project was built for [Houston's Mini-hackathon](http://www.minihackathon.net/) Sat, November 4, 2017.

## Tech Stack
- Python 3.6
- Tornado web framework
- PostgreSQL
- google heatmap

## Installation Instructions
1. git clone repository
2. `cd fresh-finder`
3. Install dependecies: `pip install -r requirements.txt`
4. Environment variables:
- export APP_SETTINGS="config.DevelopmentConfig"
- export DATABASE_URL="postgresql://localhost/transport_db"
5. Run app: `python3 app.py`

## Developers Journal
- Wow, this hackathon was probably the most eventful one of all! I thought a mini-hacakthon would be easier but it's actually 100x harder!
- My team and I originally wanted to create a program that scrapes twitter for tweet coordinates. Then map the coordinates on a heatmap to visualize trending topics.
- Eight hours was not nearly enough time.
- At first, we wanted to use Elasticsearch with Kibana as a visualization board. Nobody on the team had any experience with Elasticsearch. We realized the task was way out of MVP.
- We did not anticipate that almost all tweets do not have coordinates.
- Since we completed building the infrastructure of the project, we found a csv file of farmers market coordinates. Converted it to geoJSON and mapped that.

-----
### Inspiration
Many people want locally grown food but many farmers markets schedules and vendors change regularly. By aggregating all the farmers markets into one convenient interactive map, we can connect people to locally grown fresh food. This helps the local economy and the local vendors from throwing away fresh food. And it’s a great place for someone new in the city to meet the community.

### What it does
It plots given data and shows relevant information for farmers markets in your area

### How I built it
It was built using a Flask framework with a Python backend. We used a javascript frontend to process geoJson data and display into the google maps API.

### Challenges we ran into
It was extremely difficult to find the right data. Also, half way through the mini-hackathon, we had to pivot our project model away from social media due to the limitations of the available API’s.

### Accomplishments that I’m proud of
It works!

We have a functioning proof of concept that we can build on. :smiley:

### What I learned
API limitations can severely restrict project outcomes and the importance of scoping a project appropriately to the timeframe.

### What’s next for Fresh Finder
We hope to get a better dataset. Add filtering of the data so users can look specific vendors, types of vendors, and food type.
