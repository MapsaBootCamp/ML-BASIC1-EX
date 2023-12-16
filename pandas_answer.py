import pandas as pd

trips_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client', 'completed', 'completed', 'completed', 'completed', 'completed', 'cancelled_by_driver'],
    'request_at': ['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01', '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03', '2013-10-03', '2013-10-03']
})

users_df = pd.DataFrame({
    'users_id': [1, 2, 3, 4, 10, 11, 12, 13],
    'banned': [False, True, False, False, False, False, False, False],
    'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver']
})

clients = users_df[users_df["role"] == "client"].iloc[:, :-1]
drivers = users_df[users_df["role"] == "driver"].iloc[:, :-1]

clients.rename(columns={"users_id": "client_id", "banned": "client_banned"}, inplace=True)
drivers.rename(columns={"users_id": "driver_id", "banned": "driver_banned"}, inplace=True)

df = pd.merge(trips_df, clients, on="client_id")
df = pd.merge(df, drivers, on="driver_id")

df_unbanned = df[(df["client_banned"] == False) & (df["driver_banned"] == False)]

def func(group):
    group["Cancellation Rate"] = round(len(group[group["status"] != "completed"]) / len(group), 2)
    return group.iloc[0]

output = df_unbanned.groupby("request_at", as_index=False).apply(func)
output.rename(columns={"request_at": "Day"} ,inplace=True)
output = output[["Day", "Cancellation Rate"]]
print(output)