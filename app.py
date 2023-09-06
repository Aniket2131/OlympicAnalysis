import streamlit as st
import pandas as pd
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df_summer = preprocessor.preprocessor(df, region_df, "Summer")
df_winter = preprocessor.preprocessor(df, region_df, "Winter")

st.sidebar.title("Report On Olympic")
olympics = 'Summer'
olympic = st.sidebar.radio(
    'Select an Option',
    ('Summer', 'Winter')
)

# menu = 'Medal Tally'

menu = st.sidebar.radio(
    'Select an analysis type',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis')
)


if olympic == 'Summer' and menu == 'Medal Tally':
    # st.sidebar.header('Medal Tally')

    year, country = helper.country_year_list(df_summer)

    selected_country = st.sidebar.selectbox('Select Country', country)
    selected_year = st.sidebar.selectbox('Select Year', year)

    medal_tally = helper.get_year_country_data(df_summer, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title("Medals of " + selected_country)

    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medals of " + str(selected_year))

    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title("Medals of " + selected_country + "in" + str(selected_year))

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Summer Overall Medals")

    st.table(medal_tally)

if olympic == 'Summer' and menu == 'Overall Analysis':
    country = df_summer['region'].nunique()
    host_country = df_summer['City'].nunique()
    players = df_summer['Name'].nunique()
    edition = df_summer['Year'].nunique()
    sport = df_summer['Sport'].nunique()
    event = df_summer['Event'].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Country")
        st.title(country)

    with col2:
        st.header("City")
        st.title(host_country)

    with col3:
        st.header("Players")
        st.title(players)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Edition")
        st.title(edition)

    with col2:
        st.header("Sports")
        st.title(sport)

    with col3:
        st.header("Events")
        st.title(event)

    st.title("No of Countries participating over the years")
    helper.plot_line_graph(df_summer, 'region', "Year", "No of Country")
    st.title("No of Events over the years")
    helper.plot_line_graph(df_summer, 'Event', "Year", "No of Events")
    st.title("No of Players participating over the years")
    helper.plot_line_graph(df_summer, 'Name', "Year", "No of Players")

    st.header("Most Successful Player")
    sport_list = df_summer['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Please Select the sport', sport_list)
    temp_df = helper.get_most_successful_player(df_summer, selected_sport)
    st.table(temp_df)


if olympic == 'Summer' and menu == 'Country-wise Analysis':
    year, country = helper.country_year_list(df_summer)
    selected_country = st.selectbox("Select Country", country)
    if selected_country == "Overall":
        st.header("Year wise medals")
    else:
        st.header(selected_country + " Year wise medals")
    final_df = helper.country_medal_graph(df_summer, selected_country)
    fig, ax = plt.subplots()
    ax.plot(final_df['Year'], final_df['Medal'], linestyle='dashed', c='Brown')
    plt.xlabel("Year")
    plt.ylabel("Medal")
    st.pyplot(fig)

    pt = helper.country_sport_heatmap(df_summer, selected_country)
    if pt.shape[0] != 0 and selected_country != "Overall":
        st.title(selected_country + " Performance in each game")
        fig, ax = plt.subplots(figsize=(20, 30))
        ax = sns.heatmap(pt, annot=True)
        st.pyplot(fig)

        st.title("Top 10 players" + selected_country)
        top10 = helper.get_top_players(df_summer, selected_country)
        st.table(top10)


if olympic == 'Winter' and menu == 'Medal Tally':
    # st.sidebar.header('Medal Tally')
    year, country = helper.country_year_list(df_winter)

    selected_country = st.sidebar.selectbox('Select Country', country)
    selected_year = st.sidebar.selectbox('Select Year', year)

    medal_tally = helper.get_year_country_data(df_winter, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title("Medals of " + selected_country)

    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medals of " + str(selected_year))

    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title("Medals of " + selected_country + "in" + str(selected_year))

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Winter Overall Medals")

    st.table(medal_tally)


if olympic == 'Winter' and menu == 'Overall Analysis':
    country = df_winter['region'].nunique()
    host_country = df_winter['City'].nunique()
    players = df_winter['Name'].nunique()
    edition = df_winter['Year'].nunique()
    sport = df_winter['Sport'].nunique()
    event = df_winter['Event'].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Country")
        st.title(country)

    with col2:
        st.header("City")
        st.title(host_country)

    with col3:
        st.header("Players")
        st.title(players)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Edition")
        st.title(edition)

    with col2:
        st.header("Sports")
        st.title(sport)

    with col3:
        st.header("Events")
        st.title(event)

    st.title("No of Countries participating over the years")
    helper.plot_line_graph(df_winter, 'region', "Year", "No of Country")
    st.title("No of Events over the years")
    helper.plot_line_graph(df_winter, 'Event', "Year", "No of Events")
    st.title("No of Players participating over the years")
    helper.plot_line_graph(df_winter, 'Name', "Year", "No of Players")

    st.header("Most Successful Player")
    sport_list = df_winter['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Please Select the sport', sport_list)
    temp_df = helper.get_most_successful_player(df_winter, selected_sport)
    st.table(temp_df)


if olympic == 'Winter' and menu == 'Country-wise Analysis':
    year, country = helper.country_year_list(df_winter)
    selected_country = st.selectbox("Select Country", country)
    if selected_country == "Overall":
        st.header("Year wise medals")
    else:
        st.header(selected_country + " Year wise medals")
    final_df = helper.country_medal_graph(df_winter, selected_country)
    fig, ax = plt.subplots()
    ax.plot(final_df['Year'], final_df['Medal'], linestyle='dashed', c='Brown')
    plt.xlabel("Year")
    plt.ylabel("Medal")
    st.pyplot(fig)

    pt = helper.country_sport_heatmap(df_winter, selected_country)
    if pt.shape[0] != 0 and selected_country != "Overall":
        st.title(selected_country + " Performance in each game")
        fig, ax = plt.subplots(figsize=(20, 30))
        ax = sns.heatmap(pt, annot=True)
        st.pyplot(fig)

        st.title("Top 10 players" + selected_country)
        top10 = helper.get_top_players(df_winter, selected_country)
        st.table(top10)
