import justetf_scraping
df = justetf_scraping.load_overview()

df.to_csv("JustETF_export.csv", sep=',')


