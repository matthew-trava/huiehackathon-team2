from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from pathlib import Path

data_path = Path(__file__).parents[1] / "joyce"


def comparison_plots(x):
    if x == 'staff_service':
        title = "Changes to level of service delivered by number of paid staff within the organisation"
        return comparison_heatmap(data_path, x , title)
    if x == 'type_service':
        title = "Changes to level of service delivered by organisation service type"
        return comparison_heatmap(data_path, x , title)
    if x == 'volunteers_service':
        title = "Changes to level of service delivered by number of volunteer staff within the organisation"
        return comparison_heatmap(data_path, x , title)
    if x == 'income_service':
        title = "Changes to level of service delivered by organisation income level"
        return comparison_heatmap(data_path, x , title)
    if x == 'ethnic_service':
        title = "Changes to level of service delivered by organisation target ethnicity"
        return comparison_heatmap(data_path, x , title)
    if x == 'staff_funding':
        title = "Funding reserve level by number of paid staff within the organisation"
        return comparison_heatmap(data_path, x , title)
    if x == 'type_funding':
        title = "Funding reserve level by organisation service type"
        return comparison_heatmap(data_path, x , title)
    if x == 'volunteers_funding':
        title = "Funding reserve level by number of volunteer staff within the organisation"
        return comparison_heatmap(data_path, x , title)
    if x == 'income_funding':
        title = "Funding reserve level by organisation income level"
        return comparison_heatmap(data_path, x , title)
    if x == 'ethnic_funding':
        title = "Funding reserve level by organisation target ethnicity"
        return comparison_heatmap(data_path, x , title)
    if x == 'bar_service':
        title = "Distribution of changes to level of service delivered"
        return comparison_gbarchart(data_path, x , title)
    if x == 'bar_funding':
        title = "Distribution of funding reserve levels"
        return comparison_gbarchart(data_path, x , title)

def comparison_heatmap(data_path, chart_name, title):
    fig = make_subplots(rows=1, cols=2, subplot_titles=("2020", "2021"), horizontal_spacing=0.175)
    filename20 = 'c_' + chart_name + '_20.csv'
    filename21 = 'c_' + chart_name + '_21.csv'
    df20 = pd.read_csv(data_path / filename20, index_col=0)
    df21 = pd.read_csv(data_path / filename21, index_col=0)
    df20 = df20.iloc[::-1]
    df21 = df21.iloc[::-1]
    intersection_index = df21.index & df20.index
    df20 = df20.loc[intersection_index]
    df21 = df21.loc[intersection_index]
    index20 = df20.index.str.replace("\\$", "&#36;").str.replace("\\", "")
    index21 = df21.index.str.replace("\\$", "&#36;").str.replace("\\", "")
    fig.add_trace(go.Heatmap(
        z=df20,
        x=df20.columns,
        y=index20,
        coloraxis="coloraxis"),
        row=1, col=1
    )
    fig.add_trace(go.Heatmap(
        z=df21,
        x=df21.columns,
        y=index21,
        coloraxis="coloraxis"),
        row=1, col=2
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis={'colorscale': 'BuPu'},
                      height=len(intersection_index) * 40 + 200,
                      title_text=title,
                      yaxis2=dict(anchor='free', position=0.42,
                                  side='right'
                                  ))
    fig.update_yaxes(showticklabels=False, row=1, col=1)
    return (fig)


def comparison_gbarchart(data_path, chart_name, title):
    filename = 'c_' + chart_name + '.csv'
    df = pd.read_csv(data_path / filename, index_col=0)
    # fig = px.histogram(df, x="category", y="percentage",
    #              color='year', barmode='group',
    #              height=800, title=title, )
    df20=df[df['year'] == 2020]
    df21=df[df['year'] == 2021]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df20["category"],
        y=df20["percentage"],
        name='2020',
        marker=dict(color='rgba(55, 53, 87 ,250)'),
    ))
    fig.add_trace(go.Bar(
        x=df21["category"],
        y=df21["percentage"],
        name='2021',
        marker=dict(color='rgba(237, 19, 92 ,250)'),
    ))

    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis={'colorscale': 'BuPu'})
    return(fig)