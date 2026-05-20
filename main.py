# Main file to run the whole project

from extract import extract_data
from clean import clean_data
from model import build_model
from visualize import visualize_data


def main():
    # Extract and wrangle data
    df = extract_data()

    # Clean and inspect data
    df, corr = clean_data(df)

    # Build model and generate predictions
    model, feat_imp, y_test_pred = build_model(df)

    # Visualize data and model results
    visualize_data(df, corr, feat_imp)


if __name__ == "__main__":
    main()
