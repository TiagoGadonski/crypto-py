import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(data):
    data['price_change'] = data['price'].pct_change()
    data = data.dropna()

    X = data[['price']].shift(1).dropna()  # Usar preço anterior para prever o próximo
    y = data['price_change'].shift(-1).dropna()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    print(f"Model score: {model.score(X_test, y_test)}")

    return model
