def clean_data(df):
    #select categorical data (str data)
    df.select_dtypes("object").head()

    #list the unique values in each category to determine low & high cardinality
    #from the result operation-1,property_type-1,currency-1,properati_url-5473
    #operation, property_type, currency have low cardinality(notmore than one category) and
    #properati_url has high cardinality: so many categories of unique points
    df.select_dtypes("object").nunique()


    #check the columns and remove those that would leak data(closely related or derived from our Target Vector > price_aprox_usd)
    sorted(df.columns)

    #check for multicolinearity
    corr = df.select_dtypes("number").drop(columns="price_aprox_usd").corr()

    return df, corr
