from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
# import pickle5 as pickle
from pathlib import Path

pkl_path = Path(__file__).parents[1] / "joyce"


def comparison_plots(x):
    if x == 'staff_service':
        title = "Changes to level of service delivered by number of paid staff within the organisation"
        return comparison_heatmap(pkl_path / 'p_staff_service.pickle', title)
    if x == 'type_service':
        title = "Changes to level of service delivered by organisation service type"
        return comparison_heatmap(pkl_path / 'p_type_service.pickle', title)
    if x == 'volunteers_service':
        title = "Changes to level of service delivered by number of volunteer staff within the organisation"
        return comparison_heatmap(pkl_path / 'p_volunteers_service.pickle', title)
    if x == 'income_service':
        title = "Changes to level of service delivered by organisation income level"
        return comparison_heatmap(pkl_path / 'p_income_service.pickle', title)
    if x == 'ethnic_service':
        title = "Changes to level of service delivered by organisation target ethnicity"
        return comparison_heatmap(pkl_path / 'p_ethnic_service.pickle', title)
    if x == 'staff_funding':
        title = "Funding reserve level by number of paid staff within the organisation"
        return comparison_heatmap(pkl_path / 'p_staff_funding.pickle', title)
    if x == 'type_funding':
        title = "Funding reserve level by organisation service type"
        return comparison_heatmap(pkl_path / 'p_type_funding.pickle', title)
    if x == 'volunteers_funding':
        title = "Funding reserve level by number of volunteer staff within the organisation"
        return comparison_heatmap(pkl_path / 'p_volunteers_funding.pickle', title)
    if x == 'income_funding':
        title = "Funding reserve level by organisation income level"
        return comparison_heatmap(pkl_path / 'p_income_funding.pickle', title)
    if x == 'ethnic_funding':
        title = "Funding reserve level by organisation target ethnicity"
        return comparison_heatmap(pkl_path / 'p_ethnic_funding.pickle', title)


def comparison_heatmap(picklefilepath, title):
    fig = make_subplots(rows=1, cols=2, subplot_titles=("2020", "2021"), horizontal_spacing=0.175)
    df = pd.read_pickle(picklefilepath)
    df20 = df.loc[2020].iloc[::-1]
    df21 = df.loc[2021].iloc[::-1]
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
# df = pd.read_csv ('users21.csv', index_col=0)
# fig = px.imshow(df, text_auto=True, colorscale='Viridis')
# fig.show()
