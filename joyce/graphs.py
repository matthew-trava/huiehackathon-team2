import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Service delivery affect
tmp = pd.concat([df20.assign(year=2020), df21.assign(year=2021)]) \
    .groupby('year').apply(lambda grp: grp[['service delivery affect', 'service delivery affect index']].value_counts(normalize=True)) \
    .rename_axis(['year', 'category', 'order']).rename('percentage').reset_index().sort_values(['year', 'order']).drop(columns='order')
sns.catplot(data=tmp, kind="bar", x="category", y="percentage", hue="year",
    ci="sd", palette="dark", alpha=.6, height=6
)
plt.title('Service delivery affect')
plt.xticks(rotation=30);

# funding reserve change
tmp = pd.concat([df20.assign(year=2020), df21.assign(year=2021)]) \
    .groupby('year').apply(lambda grp: grp[['funding reserve', 'funding reserve index']].value_counts(normalize=True)) \
    .rename_axis(['year', 'category', 'order']).rename('percentage').reset_index().sort_values(['year', 'order']).drop(columns='order')
sns.catplot(data=tmp, kind="bar", x="category", y="percentage", hue="year",
    ci="sd", palette="dark", alpha=.6, height=6
)
plt.title('funding reserve change')
plt.xticks(rotation=30);
