# yearly-song-trends

This project scrapes the top songs from the past five years and maps how mentions of locations and brands as well as the mood around them change with time. Song lyrics are extracted from Genius API and sentiment analysis is conducted to determine the mood associated with each mention. These trends are visualized with interactive dashboards.

Lyricsgenius is used to to search for and retrieve song lyrics, csv and sys are used to collect and store song lyrics and develop an entities database for each song. These results will be portrayed in visualizations with matplotlib and plotly. spaCy is used to analyze the sentiment surrounding the mention of each entity. pandas and matplotlib are used for data analysis and visualization.

In the future, this analysis can be conducted over a larger time range and incorporate external data sources to justify trends, such as current events through news articles. 
