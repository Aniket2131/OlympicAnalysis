import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# def medal_tally(df):
#     total_medal = df.drop_duplicates(
#         subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
#     total_medal = total_medal.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold',
#                                                                                                 ascending=False)
#     total_medal['Total'] = total_medal['Gold'] + total_medal['Silver'] + total_medal['Bronze']
#     return total_medal


def country_year_list(df_summer1):
    years = df_summer1['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df_summer1['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, "Overall")

    return years, country


def get_year_country_data(df_summer1, year, country):
    medal_df = df_summer1.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])

    flag = 0
    if year == 'Overall' and country == 'Overall':
        res = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        res = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        res = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        res = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
    if flag == 1:
        res_df = res.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Year')
    else:
        res_df = res.groupby('NOC').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold', ascending=False)
    res_df['Total'] = res_df['Gold'] + res_df['Silver'] + res_df['Bronze']
    return res_df


def plot_line_graph(df, y_axis, x_label, y_label):
    country_over_year = df.drop_duplicates(['Year', y_axis])['Year'].value_counts().reset_index().sort_values(
        'Year')

    fig, ax = plt.subplots()
    ax.plot(country_over_year['Year'], country_over_year['count'], linestyle='dashed', c='Brown')
    # fig = plt.plot(country_over_year['Year'], country_over_year['count'], lifestyle='dashed', c='Brown')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot(fig)


def get_most_successful_player(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    res = temp_df['Name'].value_counts().reset_index().merge(df, on='Name', how='left')[
        ['Name', 'count', 'Sport', 'region']].drop_duplicates().rename(columns={'count': 'Medal'})
    return res


def country_medal_graph(df, country):
    temp = df.dropna(subset=['Medal'])
    temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp[temp['region'] == country]
    total = new_df.groupby('Year').count()['Medal'].reset_index()
    return total


def country_sport_heatmap(df, country):
    temp = df.dropna(subset=['Medal'])
    temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp[temp['region'] == country]
    total = new_df.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0)
    return total


def get_top_players(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == country]

    res = temp_df['Name'].value_counts().head(10).reset_index().merge(df, on='Name', how='left')[
        ['Name', 'count', 'Sport']].drop_duplicates().rename(columns={'count': 'Medal'})
    return res
