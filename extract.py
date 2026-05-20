# Import libraries here
import pandas as pd
import glob


# Build your `wrangle` function
#the function combines, data extraction, data cleaning and calculations
def wrangle(filepath):
    df = pd.read_csv(filepath)

    #filter out apartments in Distrito Federal that cost lest than USD 100,000
    mask_dist = df["place_with_parent_names"].str.contains("Distrito Federal")
    mask_price = df["price_aprox_usd"] < 100000
    mask_apt = df["property_type"] == "apartment"
    df = df[mask_dist & mask_price & mask_apt]

    #filter out bottom 10 and 90nth percentile..Removing outliers in the data
    low, high = df["surface_covered_in_m2"].quantile([0.1, 0.9])
    mask_area = df["surface_covered_in_m2"].between(low, high)
    df=df[mask_area]

    #separate lat-lon columns
    df[["lat","lon"]] = df["lat-lon"].str.split(",", expand=True).astype(float)
    df.drop(columns="lat-lon", inplace=True)

    #create a borough feature from the column "place_with_parent_names"
    df["borough"] = df["place_with_parent_names"].str.split("|",expand=True)[1]
    df.drop(columns="place_with_parent_names", inplace=True)

    #check the whole dataframe and drop columns with more than half missing values
    drop_columns=[]
    for column in df.columns:
        if df[column].isnull().sum() > len(df[column])/2:
            drop_columns.append(column)
        else:
            pass
    df.drop(columns=drop_columns, inplace=True)

    #drop columns with low and high cardinality
    df.drop(columns=["operation", "property_type", "currency", "properati_url"], inplace=True)

    #drop columns that would cause leakage to our model
    df.drop(
        columns=['price',
        'price_aprox_local_currency',
        'price_per_m2'],
        inplace=True
    )

    return df


def extract_data():
    #create a list of the data sources you are to pull
    files = glob.glob("data/mexico-city-real-estate-[1-5].csv")
    files

    #combine wrangle, list comprehension, pd.concat to creat one big data frame
    list_df =[wrangle(file) for file in files]
    df = pd.concat(list_df)
    print(df.info())
    df.head()

    return df
