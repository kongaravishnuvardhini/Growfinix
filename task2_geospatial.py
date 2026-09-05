
import pandas as pd
import folium
from sklearn.cluster import KMeans

# Logistics data
data = {
    "Location": [
        "Warehouse", "Delivery 1", "Delivery 2", "Delivery 3",
        "Delivery 4", "Delivery 5", "Delivery 6", "Delivery 7"
    ],
    "Latitude": [
        17.3850, 17.3950, 17.3750, 17.4100,
        17.3600, 17.4000, 17.3500, 17.4200
    ],
    "Longitude": [
        78.4867, 78.5000, 78.4700, 78.5200,
        78.4500, 78.4800, 78.5100, 78.4600
    ],
    "Delivery_Time_Min": [0, 35, 25, 60, 30, 55, 70, 40]
}

logistics_df = pd.DataFrame(data)

# Identify bottlenecks
bottlenecks = logistics_df[
    logistics_df["Delivery_Time_Min"] > 50
]

print("BOTTLENECK DELIVERIES")
print(bottlenecks[["Location", "Delivery_Time_Min"]])

# KMeans clustering
locations = logistics_df[
    logistics_df["Location"] != "Warehouse"
][["Latitude", "Longitude"]]

kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

logistics_df.loc[
    logistics_df["Location"] != "Warehouse",
    "Cluster"
] = kmeans.fit_predict(locations) + 1

# Create cluster map
cluster_map = folium.Map(
    location=[17.3850, 78.4867],
    zoom_start=13
)

for _, row in logistics_df.iterrows():

    if row["Location"] == "Warehouse":
        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            popup="Warehouse"
        ).add_to(cluster_map)

    else:
        folium.CircleMarker(
            [row["Latitude"], row["Longitude"]],
            radius=8,
            popup=(
                f"{row['Location']}<br>"
                f"Cluster: {int(row['Cluster'])}<br>"
                f"Delivery Time: {row['Delivery_Time_Min']} min"
            ),
            fill=True
        ).add_to(cluster_map)

cluster_map.save("Task-2-Cluster-Map.html")

print("Task 2 completed successfully!")
