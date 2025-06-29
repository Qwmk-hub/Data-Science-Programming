import statsmodels.api as sm

X_const = sm.add_constant(X)

ols_model = sm.OLS(y, X_const).fit()

print(ols_model.summary())
