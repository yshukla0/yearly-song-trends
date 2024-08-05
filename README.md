# yearly-song-trends
Popular music is an increasingly insightful measure of everchanging cultural trends, and by analyzing the components by which they are crafted which, we can move one step closer to understanding the public's interests and sentiments towards trademarks of popular culture and how they have changed. This analysis hopes to breakdown how the media influences and reflects societal changes. 

This project scrapes the top songs from the past five years and maps how mentions of locations, brands, and celebrities as well as the mood around them change with time. Song lyrics are extracted from Genius and sentiment analysis is conducted to determine the mood associated with each mention. These trends are visualized with interactive dashboards.

This project is programmed in Python and uses Genius API to retrieve lyrics. Top songs are extracted from kworb.net. requests, BeautifulSoup are used for webscraping, spacy and textblob are used for natural language processing, and pandas, matplotlib, and plotly are used for data analysis and visualization.

The data is processed by text cleaning and using Spacy to recognize the relevant entities at hand. Then, textblob is used to perform sentiment analysis. Trend and sentiment analysis will be conducted to observe how often these mentions and its associated mood change over time. These results will be portrayed in visualizations with matplotlib and plotly. 

In the future, this analysis can be conducted over a larger time range and incorporate external data sources to justify trends, such as current events through news articles. 
