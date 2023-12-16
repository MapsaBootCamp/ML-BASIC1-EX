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

start_date = '2013-10-01'
end_date = '2013-10-03'
filtered_trips_df = trips_df[(trips_df['request_at'] >= start_date) & (trips_df['request_at'] <= end_date)]

joined_df = filtered_trips_df.merge(users_df, left_on='client_id', right_on='users_id', how='inner')
joined_df = joined_df.merge(users_df, left_on='driver_id', right_on='users_id', how='inner')

unbanned_trips_df = joined_df[(joined_df['banned_x'] == False) & (joined_df['banned_y'] == False)]

cancellation_rate = unbanned_trips_df.groupby('request_at')['status'].apply(lambda x: ((x == 'cancelled_by_client') | (x == 'cancelled_by_driver')).sum() / len(x))

cancellation_rate = cancellation_rate.round(2)

print(cancellation_rate)
