def test_train_dataset():
    assert len(df_train) == 891
    assert all(
        col in df_train.columns
        for col in [
            "PassengerId",
            "Survived",
            "Pclass",
            "Name",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "Ticket",
            "Fare",
            "Cabin",
            "Embarked",
        ]
    )


def test_female_survival():
    fem = df_train.loc[df_train.Sex == "female"]["Survived"]
    survival_rate = sum(fem) / len(fem)
    assert abs(survival_rate - 0.74) < 0.03


def test_model_accuracy():
    assert abs(accuracy - 0.78) < 0.03


def test_prediction_for_1st_passanger():
    passenger = df_train_clean[features].loc[0]
    survival = model.predict([passenger])
    expected = df_train.loc[0]["Survived"]
    assert expected == survival[0]

