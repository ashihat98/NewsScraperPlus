import pandas as pd

def process_data(news_list):
    """ Process the news data by converting it to a DataFrame and cleaning it. """
    df = pd.DataFrame(news_list)
    if not df.empty:
        df = remove_duplicates(df)
        df = handle_missing_values(df)
        df = standardize_formats(df)
    return df

def remove_duplicates(df):
    """ Remove duplicate entries based on article titles and links. """
    return df.drop_duplicates(subset=['title', 'link'])

def handle_missing_values(df):
    """ Handle missing values - fill with a default string or remove. """
    df['title'] = df['title'].fillna('No Title Provided')
    df['link'] = df['link'].fillna('No Link Provided')
    return df

def standardize_formats(df):
    """ Standardize formats if necessary, such as date formats or string casing. """
    df['title'] = df['title'].str.title()
    return df
