import pandas as pd
from io import StringIO


def read_data_from_zip(file="titanic.zip", dataset="train"):
    from zipfile import ZipFile

    with ZipFile(file, "r") as zip:
        train = zip.read(dataset + ".csv").decode("utf-8")
    df_train = pd.read_csv(StringIO(train))
    return df_train


def preprocess_data(dataframe, features=None):
    from sklearn.preprocessing import LabelEncoder

    if features is None:
        features = list(dataframe.columns)
    df = dataframe[features]
    df = df.loc[df["Age"].notnull()]
    label_enc = LabelEncoder()
    df["Sex"] = label_enc.fit_transform(df["Sex"])
    df["Embarked"] = label_enc.fit_transform(df["Embarked"])
    return df


def train_model(data, features):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    X = data[features]
    Y = data["Survived"]
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.25, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    return model, accuracy

def save_model(model, name='titanic', destination='.'):
    import os.path as path
    import joblib
    dest = path.join(destination, f"{name}.joblib")
    joblib.dump(model, dest)
    return dest


def main():
    df_train = read_data_from_zip()

    features = ["Sex", "Age", "SibSp", "Parch", "Pclass", "Fare", "Embarked"]
    df_train_clean = preprocess_data(df_train, features=features + ["Survived"])

    model, accuracy = train_model(df_train_clean, features)
    model.accuracy = accuracy
    model.dataset = "Titanic (Kaggle)"
    model_file = save_model(model)
    print(f"Model saved to {model_file}")



if __name__ == '__main__':
    main()

