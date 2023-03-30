import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from cycler import cycler

palette = ['#3c3744', '#048BA8', '#EE6352', '#E1BB80', '#78BC61']
grey_palette = ['#8e8e93', '#636366', '#48484a', '#3a3a3c', '#2c2c2e', '#1c1c27']
bg_color = '#F6F5F5'
white_color = '#d1d1d6'

custom_params = {
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.left': False,
    'grid.alpha':0.2,
    'figure.figsize': (16, 6),
    'axes.titlesize': 'large',
    'axes.labelsize': 'large',
    'ytick.labelsize': 'medium',
    'xtick.labelsize': 'medium',
    'legend.fontsize': 'large',
    'lines.linewidth': 1,
    'axes.prop_cycle': cycler('color',palette),
    'figure.facecolor': bg_color,
    'figure.edgecolor': bg_color,
    'axes.facecolor': bg_color,
    'text.color':grey_palette[1],
    'axes.labelcolor':grey_palette[1],
    'axes.edgecolor':grey_palette[1],
    'xtick.color':grey_palette[1],
    'ytick.color':grey_palette[1],
    'figure.dpi':150,
}
sns.set_theme(
    style='whitegrid',
    palette=sns.color_palette(palette),
    rc=custom_params)


def plot_time_series(df, cols: list = None, dataframe_name: str = None, palette: object = grey_palette, savefig: bool = False):
    if cols is None:
        cols = ['AccV','AccML','AccAP']

    fig, axes = plt.subplots(3, 1, figsize=(10, 9))

    for ax, col in zip(axes.ravel(), cols):
        sns.lineplot(df, x='Time', y=col, palette=grey_palette[3], ax=ax)

    plt.subplots_adjust(hspace=0.45)
    plt.suptitle(
        f"Time Series of {dataframe_name}'s Accelerometer Features",
        ha='center',
        fontweight='bold',
        color=grey_palette[2])
    if savefig:
        plt.savefig(f'../data/images/plot_time_series_{dataframe_name}.png')
    plt.show()


def plot_count(
    df: pd.core.frame.DataFrame,
    column: str = 'Medication',
    title_name: str = 'Train',
    savefig: bool = False
) -> None:
    """
    Draws the pie and count plots for categorical variables.
    """
    f, ax = plt.subplots(1, 2, figsize=(10, 4))
    plt.subplots_adjust(wspace=0)

    s1 = df[column].value_counts()
    N = len(s1)

    outer_sizes = s1
    inner_sizes = s1 / N

    outer_colors = [palette[0], palette[0], '#ff781f', '#ff9752', '#ff9752']
    inner_colors = [palette[1], palette[1], '#ffa66b']

    ax[0].pie(
        outer_sizes,colors=outer_colors,
        labels=s1.index.tolist(),
        startangle=90,frame=True, radius=1.3,
        explode=([0.05] * (N - 1) + [.3]),
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
        textprops={'fontsize': 12, 'weight': 'bold'}
    )

    textprops = {
        'size':13,
        'weight': 'bold',
        'color':'white'
    }

    ax[0].pie(
        inner_sizes, colors=inner_colors,
        radius=1, startangle=90,
        autopct='%1.f%%',explode=([.1] * (N - 1) + [.3]),
        pctdistance=0.8, textprops=textprops
    )

    center_circle = plt.Circle((0,0), .68, color='black',
                               fc='white', linewidth=0)
    ax[0].add_artist(center_circle)

    x = s1
    y = [0, 1]
    sns.barplot(
        x=x, y=y, ax=ax[1],
        palette=palette[:2], orient='horizontal'
    )

    ax[1].tick_params(
        axis='x',
        which='both',
        bottom=False,
        labelbottom=False
    )

    for i, v in enumerate(s1):
        ax[1].text(
            v, i + 0.1, str(v), color='black',
            fontweight='bold', fontsize=12)

    plt.setp(ax[1].get_yticklabels(), fontweight="bold")
    plt.setp(ax[1].get_xticklabels(), fontweight="bold")
    ax[1].set_xlabel(column, fontweight="bold", color='black')
    ax[1].set_ylabel('count', fontweight="bold", color='black')

    f.suptitle(f'{title_name}', fontsize=20, fontweight='bold')
    plt.tight_layout()
    if savefig:
        plt.savefig(f'../data/images/plot_count_{title_name}.png')
    plt.show()
