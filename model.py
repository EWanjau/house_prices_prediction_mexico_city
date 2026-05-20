import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.impute import SimpleImputer
from category_encoders import OneHotEncoder


def build_model(df):
    # Split data into feature matrix `X_train` and target vector `y_train`.
    target = "price_aprox_usd"
    features = ["surface_covered_in_m2","lat","lon","borough"]

    X_train = df[features]
    y_train = df[target]

    y_mean = [y_train.mean()]
    y_pred_baseline = y_mean * len(y_train)
    baseline_mae = mean_absolute_error(y_train, y_pred_baseline)
    print("Mean apt price:", y_mean)
    print("Baseline MAE:", round(baseline_mae, 2))

    # Build Model
    model =make_pipeline(
        OneHotEncoder(use_cat_names=True),
        SimpleImputer(),
        Ridge()
    )
    # Fit model
    model.fit(X_train, y_train)

    X_test = pd.read_csv("data/mexico-city-test-features.csv")
    print(X_test.info())
    X_test.head()

    y_test_pred = pd.Series(model.predict(X_test))
    y_test_pred.head()


    #get the coefficients and features
    coefficients = model.named_steps["ridge"].coef_
    features = model.named_steps["onehotencoder"].get_feature_names()
    feat_imp = pd.Series(coefficients, index=features)
    feat_imp

    return model, feat_imp, y_test_pred
