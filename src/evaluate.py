from sklearn.metrics import r2_score, mean_squared_error

def evaluate(model, X_train, y_train, X_val, y_val):

    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    print("Train R2:", r2_score(y_train, train_pred))
    print("Validation R2:", r2_score(y_val, val_pred))

    print("Train MSE:", mean_squared_error(y_train, train_pred))
    print("Validation MSE:", mean_squared_error(y_val, val_pred))