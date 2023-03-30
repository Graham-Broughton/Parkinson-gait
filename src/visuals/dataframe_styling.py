import pandas as pd
from pandas.io.formats.style import Styler


# Dataframe visual helper functions
def magnify(is_test: bool = False):
    """
    Magnifies the cell when the cursor is hovering above it
    """
    base_color = '#457ea5'
    if is_test:
        highlight_target_row = []
    else:
        highlight_target_row = [
            dict(
                selector='tr:last-child',
                props=[('background-color', f'{base_color}20')],
            )
        ]

    return [dict(
        selector="th",
        props=[
            ("font-size", "11pt"),
            ('background-color', f'{base_color}'),
            ('color', 'white'),
            ('font-weight', 'bold'),
            ('border-bottom', '0.1px solid white'),
            ('border-left', '0.1px solid white'),
            ('text-align', 'right')]),

            dict(
                selector='th.blank.level0',
                props=[
                    ('font-weight', 'bold'),
                    ('border-left', '1.7px solid white'),
                    ('background-color', 'white')]),

            dict(
                selector="td",
                props=[
                    ('padding', "0.5em 1em"),
                    ('text-align', 'right')]),

            dict(
                selector="th:hover",
                props=[
                    ("font-size", "14pt")]),

            dict(
                selector="tr:hover td:hover",
                props=[
                    ('max-width', '250px'),
                    ('font-size', '14pt'),
                    ('color', f'{base_color}'),
                    ('font-weight', 'bold'),
                    ('background-color', 'white'),
                    ('border', f'1px dashed {base_color}')]),

            dict(
                selector="caption",
                props=[
                    (('caption-side', 'bottom'))])] + highlight_target_row


def stylize_describe(df: pd.DataFrame, dataset_name: str = 'train', is_test: bool = False) -> Styler:
    """
    Applies .describe() method to the df and wraps it into the Styler.
    """

    s = df.describe().T
    # A formatting dictionary for controlling each column precision (.000 <-).
    cols = s.index.tolist()
    nulls = df[cols].isnull().sum()

    s['NaN count'] = nulls

    di_frmt = {
        (i if i == 'count' else i):
        ('{:.0f}' if i == 'count' else '{:.3f}') for i in s.columns}

    s = s.style.set_table_styles(magnify(is_test))\
        .format(di_frmt)\
        .set_caption(f"The {dataset_name} dataset descriptive statistics (hover to magnify).")
    return s


def stylize_simple(df: pd.DataFrame, caption: str) -> Styler:
    """
    Wraps the min_max_count pivot_table into the Styler.
    """
    s = df
    s = s.style.set_table_styles(magnify(True)).set_caption(f"{caption}")
    return s
