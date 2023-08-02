# YouTube Bot Sentiment Analysis

Interested by public attitudes toward radical climate activism (think that time when protestors threw tomato soup at a Van Gogh painting and glued themselves to the museum wall), I created a bot to scrape comments from YouTube videos about protests staged by UK-based radical climate activist group 'Just Stop Oil' to conduct a sentiment analysis. Utilizing YouTube's Data API v3, the bot extracts comments from any YouTube video given a unique video ID. To further the analysis, I exclusively selected YouTube videos from the channels of various UK news organizations with different ideological slants to explore the potential link between sentiment and ideological affiliation. After the bot scrapes the comments under a given YouTube video, it utilizes TextBlob's Natural Language Processing Library to classify comments based on sentiment and polarity and exports this data to a CSV file, which is then utilized to produce the sentiment analysis.

[![Watch the video](https://img.youtube.com/vi/LTdquzu-BXg/0.jpg)](https://www.youtube.com/watch?v=LTdquzu-BXg)


## Limitations
While the limitations of this analysis are many, the most important limitation is the accuracy of the TextBlob Natural Language Processing Library. Particularly, as is the case with the vast majority of natural language processing models that exist today, the TextBlob NLP Library is not so good at detecting sarcasm in text. As a result, many comments that clearly express a negative sentiment to a human reader are indicated as possessing a positive sentiment in the analysis. Additional limitations, among others, include the fact that one person could make numerous comments on a single video (and with different accounts), and that the relationship between someone's political affiliation and which news organizations they watch on YouTube is not so clear.

## Technologies Used
- YouTube Data API v3
- Python
- TextBlob NLP Library
- Scikit-learn
