
"""
Defines the TradeData class for processing and analyzing high-frequency trade data.
"""

import pandas as pd
from typing import Optional, List, Dict

class TradeData:
    def __init__(
        self,
        data: pd.DataFrame | str,
        price_col: str = "price",
        quantity_col: str = "quantity",
        side_col: Optional[str] = None,
        column_map: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize a TradeData object.

        Parameters
        ----------
        data : DataFrame or str
            Trade data or path to CSV file.
        price_col : str
            Name of price column.
        quantity_col : str
            Name of quantity column.
        side_col : str, optional
            Column indicating buy/sell side.
        column_map : dict, optional
            Dictionary to map standard names to custom ones.
        """
        self.data = self._load_data(data)
        self.column_map = column_map or {}
        self.price_col = price_col
        self.quantity_col = quantity_col
        self.side_col = side_col
        self._apply_column_map()

    def _load_data(self, data: pd.DataFrame | str) -> pd.DataFrame:
        if isinstance(data, str):
            return pd.read_csv(data)
        return data

    def _apply_column_map(self):
        self.data.rename(columns=self.column_map, inplace=True)

    def __call__(self, measures: List[str], freq: str = "1D") -> pd.DataFrame:
        """
        Compute multiple trade-based measures.
        """
        return pd.DataFrame()  # TODO
