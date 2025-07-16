
# Gentrification Data Lab

This project is a hands-on data journalism toolkit designed to help investigative journalists analyze real estate sales data to uncover gentrification patterns in U.S. cities.

It uses cleaned data scraped from Redfin's "Sold" listings and provides an interactive environment (Google Colab + pandas) for filtering, analyzing, and visualizing trends by ZIP code, neighborhood, and time.

---

## Purpose

**Investigative Goal:**  
Track how neighborhoods are changing by identifying:
- Rising property values
- Investor (LLC) purchases
- Flipping patterns
- Price per sq. ft. inflation
- ZIP code-specific trends

This is ideal for stories about:
- Displacement and affordability
- Predatory investment or redevelopment
- Uneven neighborhood development

---

## What's Inside

| Folder/File | Description |
|-------------|-------------|
| `data/redfin_sample.csv` | Sample sold listings data scraped from Redfin |
| `notebooks/interactive_analysis.ipynb` | Main Colab notebook with step-by-step filtering, charts, and trend detection |
| `README.md` | This file |
| `docs/` | Optional guides or project handouts |
| `tools/` | Scripts for cleaning or extending dataset with public records |
| `wiki/` | Learning material for understanding python functions |
---

## Requirements

- [Google Colab](https://colab.research.google.com)
- [Instant Data Scraper](https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah?hl=en-US)
- Python 3 (via Google Colab or Jupyter)
- Pandas
- Matplotlib or Seaborn (Packages already available in Colab)
- [Parsehub](https://www.parsehub.com) (Optional, alternative web scraping tool)

---

## How to Use This Project

1. Open the `interactive_analysis.ipynb` notebook in Google Colab
2. Clean and explore the real estate dataset
3. Choose a ZIP code or neighborhood of interest
4. Visualize price trends, buyer types, and price per square foot
5. Record your insights, leads, or story angles

---

## Reporting Ideas

- What ZIP codes saw the highest jump in sale price per sq. ft?
- Are majority of the buyers individuals or LLCs?
- Do any LLCs appear repeatedly across the dataset?
- Is there a neighborhood or zip code where homes are flipping rapidly?
- What do the trends suggest about affordability and access?

---

## Learn More

- [ProPublica – Follow the Money Reporting Guide](https://www.propublica.org/datastore/dataset/follow-the-money-reporting-guide)

---

## Contributing

If you're a journalist, educator, or developer interested in housing equity, feel free to contribute to the project. Add new data sources, improve visualizations, or adapt for other cities.

---

## Disclaimer

This project is for educational and non-commercial use only. Redfin data is used under fair use for instructional and journalistic development purposes.
