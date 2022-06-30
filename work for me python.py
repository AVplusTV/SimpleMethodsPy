"""When you so lasy but smart"""
import pyautogui as pyd
from time import sleep

sleep(7)

pyd.typewrite('"""Work for me my lovely Python!"\n'
              'import pandas as pd\n'
              'print()\n'
              'df = pd.read_csv("csv_from_anywhere.csv")\n'
              'print("Information about dataframe")\n'
              'df.info()\n'
              'print("Ten brand new rows")\n'
              'display(df.head(10))\n'
              'print("Information about colomns of table")\n'
              'display(df.column)\n'
              'print("Information about NaN cells")\n'
              'display(df.isna().sum())\n'
              'print("Information about duplicated rows")\n'
              'display(df.duplicated().sum())\n'
              'print("Information about correlations")\n'
              'display(df.corr())\n'
              'print("Description of digital data")\n'
              'display(df.describe())\n'
              '"""When you so lasy but smart"'
              , interval=0.03)