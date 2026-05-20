import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def visualize_data(df, corr, feat_imp):
    sns.heatmap(corr)

    #visualize the distribution of Apartment prices from the dataset
    fig, ax = plt.subplots()

    # Plot the histogram on the axes object
    ax.hist(df["price_aprox_usd"])

    # Label axes using the axes
    ax.set_xlabel("Price [$]")
    ax.set_ylabel("Count")


    # Add title
    ax.set_title("Distribution of Apartment Prices")
    plt.show()

    #Create a scatter plot that shows apartment price ("price_aprox_usd") as a function of apartment size ("surface_covered_in_m2")

    fig, ax = plt.subplots()

    # Create the scatter plot on the axes object
    ax.scatter(x=df["surface_covered_in_m2"], y=df["price_aprox_usd"])

    # Label axes
    ax.set_xlabel("Area [sq meters]")
    ax.set_ylabel("Price [USD]")

    #  Add title
    ax.set_title("Mexico City: Price vs. Area")
    plt.show()

    # Plot Mapbox location and price, to view the distribution by color

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        width=900,
        height=600,
        color="price_aprox_usd",
        mapbox_style="open-street-map"
    )
    fig.show()

    fig, ax = plt.subplots()

    # Create the horizontal bar plot on the axes object
    feat_imp.sort_values(key=abs).tail(10).plot(kind="barh", ax=ax)

    #  Label axes
    ax.set_xlabel("Importance [USD]")
    ax.set_ylabel("Feature")

    # Add title
    ax.set_title("Feature Importances for Apartment Price")
    plt.show()
