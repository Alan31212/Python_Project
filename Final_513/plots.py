from data import *
import matplotlib.pyplot as plt
import seaborn as sns

# create the crime trend over time
def plot_crime_trend(df):
    
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    crime_trend = df['primary_type'].resample('M').count()

    plt.figure(figsize=(10, 6))
    crime_trend.plot(kind='line', marker='o', color='red')
    plt.xlabel('Month')
    plt.ylabel('Number of Crimes')
    plt.title('Crime Trend')
    plt.grid(True)
    plt.show()

#create the crime type by month
def Crime_Type_by_Month (df):
    df['month'] = df['date'].dt.month_name()
    crime_by_month = df.groupby(['month', 'primary_type']).size().unstack()

    plt.figure(figsize=(12, 8))
    crime_by_month.plot(kind='bar', stacked=True)
    plt.xlabel('Month')
    plt.ylabel('Number of Crimes')
    plt.title('Crime Type by Month')
    plt.legend(title='Crime Type', bbox_to_anchor=(1, 1))
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.show()

#create the crime distribution by time of day
def plot_crime_by_time(df):

    df['hour'] = df['date'].dt.hour

    plt.figure(figsize=(8, 6))
    plt.hist(df['hour'], bins=24, color='yellow', edgecolor='black')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Crimes')
    plt.title('Crime Distribution by Time of Day')
    plt.xticks(range(24))
    plt.grid(axis='y')
    plt.show()

#create the top locations for different crime types
def plot_top_locations(df):
  
    top_locations = df['block'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top_locations.plot(kind='barh', color='purple')
    plt.xlabel('Number of Crimes')
    plt.ylabel('Location')
    plt.title('Top 10 Locations for Different Crime Types')
    plt.grid(axis='x')
    plt.show()


def plot_violin_plot(df):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='primary_type', y='crime_count', data=df)
    plt.xlabel('Crime Type')
    plt.ylabel('Crime Count')
    plt.title('Crime Count Distribution by Type')
    plt.xticks(rotation=45)
    plt.show()

