import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Load and process the dataframe
dataframe = pd.read_csv("Foodure data .csv")

# Clean and convert the 'rate' column
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

# Create Streamlit app
st.title("Foodure Data Analysis Dashboard")
st.write("This dashboard provides insights on Foodure restaurant data including ratings, votes, and online order availability.")

# Sidebar for filtering options
st.sidebar.title("Filter Options")
restaurant_type = st.sidebar.multiselect("Select Restaurant Type", options=dataframe['listed_in(type)'].unique())
online_order = st.sidebar.multiselect("Select Online Order Availability", options=dataframe['online_order'].unique())

# Filtered dataframe
filtered_data = dataframe[
    (dataframe['listed_in(type)'].isin(restaurant_type)) &
    (dataframe['online_order'].isin(online_order))
]

st.sidebar.subheader("Data Summary")
st.sidebar.write(f"Number of rows in filtered data: {len(filtered_data)}")

# Visualization options
st.sidebar.subheader("Visualization Options")
selected_plot = st.sidebar.selectbox(
    "Select Plot Type",
    ["Countplot of Restaurant Type", "Votes vs Restaurant Type", "Online Order Availability", "Ratings Distribution", "Boxplot of Rate by Online Order", "Heatmap of Restaurant Type vs Online Order", "Interactive Scatter Plot", "Correlation Heatmap"]
)

# Plotting
if selected_plot == "Countplot of Restaurant Type":
    plt.figure(figsize=(10, 6))
    palette = sns.color_palette("Set2", len(dataframe['listed_in(type)'].unique()))
    sns.countplot(x=dataframe['listed_in(type)'], palette=palette)
    plt.xlabel("Type of restaurant")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Votes vs Restaurant Type":
    plt.figure(figsize=(10, 6))
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.plot(result, c="green", marker="o")
    plt.xlabel("Type of restaurant", c="blue", size=20)
    plt.ylabel("Votes", c="blue", size=20)
    plt.title("Votes vs Restaurant Type")
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Online Order Availability":
    plt.figure(figsize=(10, 6))
    sns.countplot(x=dataframe['online_order'], palette=['#3498db', '#e74c3c'])
    plt.xlabel('Online Order', c='blue', size=15)
    plt.ylabel('Count', c='blue', size=15)
    plt.title('Count of Online Order Availability', c='purple', size=18)
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Ratings Distribution":
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe['rate'], bins=5, color='#ADD8E6')  # Light blue color for the bars
    plt.title("Ratings Distribution")
    plt.xlabel("Rating")  # Adding an x-label for better clarity
    plt.ylabel("Frequency")  # Adding a y-label for better clarity
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Boxplot of Rate by Online Order":
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe, palette={'Yes': '#1f77b4', 'No': '#ff7f0e'})
    plt.xlabel('Online Order', fontsize=12)
    plt.ylabel('Rate', fontsize=12)
    plt.title('Boxplot of Rate by Online Order', fontsize=15)
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Heatmap of Restaurant Type vs Online Order":
    plt.figure(figsize=(10, 6))
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
    plt.title("Heatmap of Restaurant Type vs Online Order")
    plt.xlabel("Online Order")
    plt.ylabel("Listed In (Type)")
    st.pyplot(plt.gcf())
    plt.close()

elif selected_plot == "Interactive Scatter Plot":
    # Create the interactive scatter plot with color assigned to 'online_order'
    fig = px.scatter(dataframe, 
                     x='votes', 
                     y='rate', 
                     color='online_order',  # Use the 'online_order' column for color
                     color_discrete_map={'Yes': 'rgb(51, 204, 51)', 'No': 'red'},  # Map specific colors
                     size='votes', 
                     hover_name='name',
                     title='Votes vs Rate by Online Order', 
                     labels={'rate': 'Rating', 'votes': 'Votes'})
    
    st.plotly_chart(fig)


elif selected_plot == "Correlation Heatmap":
    plt.figure(figsize=(10, 8))
    corr = dataframe.select_dtypes(include=[np.number]).corr()  # Only numeric columns for correlation
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title('Correlation Heatmap of Numeric Features')
    st.pyplot(plt.gcf())
    plt.close()

# Streamlit data table
st.sidebar.subheader("Data Table")
st.dataframe(filtered_data)

# Ensure the Streamlit app is running with `streamlit run your_script.py`
