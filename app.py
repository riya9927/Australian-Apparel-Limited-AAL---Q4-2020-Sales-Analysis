import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load and Clean Data
@st.cache_data
def load_data():
    df = pd.read_csv("AusApparalSales4thQrt2020.csv")
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%b-%Y")
    df['Time'] = df['Time'].str.strip().str.capitalize()
    df['State'] = df['State'].str.strip().str.upper()
    df['Group'] = df['Group'].str.strip().str.capitalize()
    return df

df = load_data()

# Sidebar Filters with "All" Options
st.sidebar.header("🔎 Filter Data")

state_options = ['All'] + sorted(df["State"].unique().tolist())
group_options = ['All'] + sorted(df["Group"].unique().tolist())
time_options = ['All'] + sorted(df["Time"].unique().tolist())

selected_state = st.sidebar.selectbox("Select State", options=state_options)
selected_group = st.sidebar.selectbox("Select Group", options=group_options)
selected_time = st.sidebar.selectbox("Select Time of Day", options=time_options)

# Apply filters
filtered_df = df.copy()
if selected_state != 'All':
    filtered_df = filtered_df[filtered_df["State"] == selected_state]
if selected_group != 'All':
    filtered_df = filtered_df[filtered_df["Group"] == selected_group]
if selected_time != 'All':
    filtered_df = filtered_df[filtered_df["Time"] == selected_time]


# Metrics Overview
st.title("🛍️ Apparel Sales Dashboard - Q4 2020")
st.markdown("Explore sales by state, group, and time using interactive filters.")

total_sales = filtered_df["Sales"].sum()
total_units = filtered_df["Unit"].sum()
avg_sales = filtered_df["Sales"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Units", f"{total_units}")
col3.metric("Avg Sale / Record", f"${avg_sales:,.0f}")

# Visualizations
st.subheader("📊 Sales Distribution")

# Sales by Group
if selected_group == "All":
    group_data = filtered_df.groupby("Group")["Sales"].sum().sort_values()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=group_data.index, y=group_data.values, palette="viridis", ax=ax1)
    ax1.set_title("Total Sales by Customer Group")
    st.pyplot(fig1)

# Sales by State
if selected_state == "All":
    state_data = filtered_df.groupby("State")["Sales"].sum().sort_values()
    fig2, ax2 = plt.subplots()
    sns.barplot(x=state_data.index, y=state_data.values, palette="plasma", ax=ax2)
    ax2.set_title("Total Sales by State")
    st.pyplot(fig2)

# Sales by Time
if selected_time == "All":
    time_data = filtered_df.groupby("Time")["Sales"].sum()
    fig3, ax3 = plt.subplots()
    sns.barplot(x=time_data.index, y=time_data.values, palette="cubehelix", ax=ax3)
    ax3.set_title("Total Sales by Time of Day")
    st.pyplot(fig3)

# Daily Sales Trend
st.subheader("📈 Daily Sales Trend")

daily_sales = filtered_df.groupby("Date")["Sales"].sum()
fig4, ax4 = plt.subplots(figsize=(10, 4))
daily_sales.plot(ax=ax4, marker='o', color='teal')
ax4.set_title("Daily Sales Over Time")
ax4.set_ylabel("Sales")
ax4.set_xlabel("Date")
ax4.grid(True)
st.pyplot(fig4)

# Forecasting with Prophet (Filtered)
st.subheader("🔮 Forecast Future Sales")

forecast_df = filtered_df.groupby("Date")["Sales"].sum().reset_index()
forecast_df.columns = ["ds", "y"]

if len(forecast_df) >= 2:
    model = Prophet()
    model.fit(forecast_df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    st.write("Forecasting the next 30 days based on filtered data...")
    fig5 = model.plot(forecast)
    st.pyplot(fig5)
else:
    st.warning("Not enough data for forecasting with current filters.")

# Clustering (KMeans)
st.subheader("Sales Segmentation (KMeans)")

features = df[["Unit", "Sales"]]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=42)
df["Cluster"] = kmeans.fit_predict(scaled_features)

cluster_avg = df.groupby("Cluster")[["Unit", "Sales"]].mean()
st.write("### Average Metrics by Cluster")
st.dataframe(cluster_avg.style.format({"Unit": "{:.2f}", "Sales": "${:.2f}"}))


