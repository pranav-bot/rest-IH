import pandas as pd

data = pd.read_excel("./data.xlsx")

# Export this
quantity_per_day = data.groupby(['order_date'])["quantity"].sum().reset_index()
print(quantity_per_day.shape)
quantity_per_day['order_date'] = pd.to_datetime(data['order_date'])
quantity_per_day.to_json("quantity_per_day")

# Export This
data['year'] = pd.DatetimeIndex(
    data['order_date']).year
data['month'] = pd.DatetimeIndex(
    data['order_date']).month_name()
data['weekday'] = pd.DatetimeIndex(
    data['order_date']).day_name()
data['order_hour'] = data['order_time']
for i in range(len(data)):
    data['order_hour'].iloc[i] = data['order_time'].values[i].hour
peak_weekdays = data['weekday'].value_counts()
peak_months = data.groupby(
    ['month'])['quantity'].sum().sort_values(ascending=False)
peak_hours = data['order_hour'].value_counts()
sales_per_pizza = data.groupby(['pizza_name'])[
    'quantity'].sum().sort_values(ascending=False)
sales_by_size = data.groupby(['pizza_size'])[
    'quantity'].sum().sort_values(ascending=False)
sales_by_category = data.groupby(['pizza_category'])[
    'quantity'].sum().sort_values(ascending=False)
sales_by_quantity = data['quantity'].value_counts()
large_orders = data[data['pizza_size'] == 'L']['pizza_name'].value_counts()
medium_orders = data[data['pizza_size'] == 'M']['pizza_name'].value_counts()
small_orders = data[data['pizza_size'] == 'S']['pizza_name'].value_counts()
peak_weekdays.to_json("peak_weekdays")
peak_months.to_json("peak_months")
peak_hours.to_json("peak_hours")
sales_per_pizza.to_json("sales_per_pizza")
sales_by_size.to_json("sales_by_size")
sales_by_category.to_json("sales_by_category")
sales_by_quantity.to_json("sales_by_quantity")
large_orders.to_json("large_orders")
medium_orders.to_json("medium_orders")
small_orders.to_json("small_orders")
