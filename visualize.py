import matplotlib.pyplot as plt

years = data['date']
plt.plot(years[-13:], y[-13:], label='Actual', marker='o')      # 실제값
plt.plot(years[-13:], y_pred, label='Predicted', marker='x')    # 예측값
plt.title('Actual vs Predicted Glacial Volume')
plt.xlabel('Year')
plt.ylabel('Glacial Volume')
plt.legend()
plt.grid()
plt.show()
