from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
def comparison_heatmap(picklefilepath):
        fig = make_subplots(rows=1, cols=2)
        df = pd.read_pickle(picklefilepath)
        df20 = df.loc[2020].iloc[::-1]
        df21 = df.loc[2021].iloc[::-1]
        # intersection_index = df21.index & df20.index
        # df20 = df20.iloc[intersection_index]
        # df21 = df21.iloc[intersection_index]
        index20 = df20.index.str.replace("\\$", "&#36;").str.replace("\\", "")
        index21 = df21.index.str.replace("\\$", "&#36;").str.replace("\\", "")
        fig.add_trace(go.Heatmap(
                z=df20,
                x=df20.columns,
                y=index20,
                colorscale='Viridis'),
                row=1, col=1
        )
        fig.add_trace(go.Heatmap(
                z=df21,
                x=df21.columns,
                y=index21,
                colorscale='Viridis'),
                row=1, col=2
        )
        return (fig)
def comparison_plots(x):
        if x == 'staff_service':
                return comparison_heatmap('joyce/p_staff_service.pickle')
        if x == 'type_service':
                return comparison_heatmap('joyce/p_type_service.pickle')
        if x == 'volunteers_service':
                return comparison_heatmap('joyce/p_volunteers_service.pickle')
        if x == 'funding_service':
                return comparison_heatmap('joyce/p_funding_service.pickle')


# df = pd.read_csv ('users21.csv', index_col=0)
# fig = px.imshow(df, text_auto=True, colorscale='Viridis')
# fig.show()