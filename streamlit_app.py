{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data handling and visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "id": "P6Eu1OzLjl5-"
   },
   "outputs": [],
   "source": [
    "# data handling and visualization\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Import CSV, make columns lowercase and strip whitespacce"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/62/h1vk7lw13g73qsk07s3l1cwm0000gn/T/ipykernel_24611/2243734017.py:1: DtypeWarning: Columns (19,20) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv('/Users/emjack5/Desktop/Data analysis/Capstone2 files/US Airline Flight Routes and Fares 1993-2024.csv')\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv('/Users/emjack5/Desktop/Data analysis/Capstone2 files/US Airline Flight Routes and Fares 1993-2024.csv')\n",
    "\n",
    "df_raw = df.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns = df.columns.str.strip().str.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "geocoded_city1 geocoded_city2\n"
     ]
    }
   ],
   "source": [
    "print(df.columns[19], df.columns[20])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['geocoded_city1'] = df['geocoded_city1'].astype('string')\n",
    "df['geocoded_city2'] = df['geocoded_city2'].astype('string')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>citymarketid_1</th>\n",
       "      <th>citymarketid_2</th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>airportid_1</th>\n",
       "      <th>airportid_2</th>\n",
       "      <th>airport_1</th>\n",
       "      <th>airport_2</th>\n",
       "      <th>...</th>\n",
       "      <th>fare</th>\n",
       "      <th>carrier_lg</th>\n",
       "      <th>large_ms</th>\n",
       "      <th>fare_lg</th>\n",
       "      <th>carrier_low</th>\n",
       "      <th>lf_ms</th>\n",
       "      <th>fare_low</th>\n",
       "      <th>geocoded_city1</th>\n",
       "      <th>geocoded_city2</th>\n",
       "      <th>tbl1apk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>30135</td>\n",
       "      <td>33195</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>10135</td>\n",
       "      <td>14112</td>\n",
       "      <td>ABE</td>\n",
       "      <td>PIE</td>\n",
       "      <td>...</td>\n",
       "      <td>81.43</td>\n",
       "      <td>G4</td>\n",
       "      <td>1.0000</td>\n",
       "      <td>81.43</td>\n",
       "      <td>G4</td>\n",
       "      <td>1.0000</td>\n",
       "      <td>81.43</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>202131013514112ABEPIE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>30135</td>\n",
       "      <td>33195</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>10135</td>\n",
       "      <td>15304</td>\n",
       "      <td>ABE</td>\n",
       "      <td>TPA</td>\n",
       "      <td>...</td>\n",
       "      <td>208.93</td>\n",
       "      <td>DL</td>\n",
       "      <td>0.4659</td>\n",
       "      <td>219.98</td>\n",
       "      <td>UA</td>\n",
       "      <td>0.1193</td>\n",
       "      <td>154.11</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>202131013515304ABETPA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>30140</td>\n",
       "      <td>30194</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>10140</td>\n",
       "      <td>11259</td>\n",
       "      <td>ABQ</td>\n",
       "      <td>DAL</td>\n",
       "      <td>...</td>\n",
       "      <td>184.56</td>\n",
       "      <td>WN</td>\n",
       "      <td>0.9968</td>\n",
       "      <td>184.44</td>\n",
       "      <td>WN</td>\n",
       "      <td>0.9968</td>\n",
       "      <td>184.44</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>202131014011259ABQDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>30140</td>\n",
       "      <td>30194</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>10140</td>\n",
       "      <td>11298</td>\n",
       "      <td>ABQ</td>\n",
       "      <td>DFW</td>\n",
       "      <td>...</td>\n",
       "      <td>182.64</td>\n",
       "      <td>AA</td>\n",
       "      <td>0.9774</td>\n",
       "      <td>183.09</td>\n",
       "      <td>AA</td>\n",
       "      <td>0.9774</td>\n",
       "      <td>183.09</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>202131014011298ABQDFW</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>30140</td>\n",
       "      <td>30466</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Phoenix, AZ</td>\n",
       "      <td>10140</td>\n",
       "      <td>14107</td>\n",
       "      <td>ABQ</td>\n",
       "      <td>PHX</td>\n",
       "      <td>...</td>\n",
       "      <td>177.11</td>\n",
       "      <td>WN</td>\n",
       "      <td>0.6061</td>\n",
       "      <td>184.49</td>\n",
       "      <td>AA</td>\n",
       "      <td>0.3939</td>\n",
       "      <td>165.77</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>202131014014107ABQPHX</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 22 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   year  quarter  citymarketid_1  citymarketid_2  \\\n",
       "0  2021        3           30135           33195   \n",
       "1  2021        3           30135           33195   \n",
       "2  2021        3           30140           30194   \n",
       "3  2021        3           30140           30194   \n",
       "4  2021        3           30140           30466   \n",
       "\n",
       "                            city1                          city2  airportid_1  \\\n",
       "0  Allentown/Bethlehem/Easton, PA  Tampa, FL (Metropolitan Area)        10135   \n",
       "1  Allentown/Bethlehem/Easton, PA  Tampa, FL (Metropolitan Area)        10135   \n",
       "2                 Albuquerque, NM          Dallas/Fort Worth, TX        10140   \n",
       "3                 Albuquerque, NM          Dallas/Fort Worth, TX        10140   \n",
       "4                 Albuquerque, NM                    Phoenix, AZ        10140   \n",
       "\n",
       "   airportid_2 airport_1 airport_2  ...    fare  carrier_lg  large_ms fare_lg  \\\n",
       "0        14112       ABE       PIE  ...   81.43          G4    1.0000   81.43   \n",
       "1        15304       ABE       TPA  ...  208.93          DL    0.4659  219.98   \n",
       "2        11259       ABQ       DAL  ...  184.56          WN    0.9968  184.44   \n",
       "3        11298       ABQ       DFW  ...  182.64          AA    0.9774  183.09   \n",
       "4        14107       ABQ       PHX  ...  177.11          WN    0.6061  184.49   \n",
       "\n",
       "   carrier_low   lf_ms fare_low  geocoded_city1  geocoded_city2  \\\n",
       "0           G4  1.0000    81.43            <NA>            <NA>   \n",
       "1           UA  0.1193   154.11            <NA>            <NA>   \n",
       "2           WN  0.9968   184.44            <NA>            <NA>   \n",
       "3           AA  0.9774   183.09            <NA>            <NA>   \n",
       "4           AA  0.3939   165.77            <NA>            <NA>   \n",
       "\n",
       "                 tbl1apk  \n",
       "0  202131013514112ABEPIE  \n",
       "1  202131013515304ABETPA  \n",
       "2  202131014011259ABQDAL  \n",
       "3  202131014011298ABQDFW  \n",
       "4  202131014014107ABQPHX  \n",
       "\n",
       "[5 rows x 22 columns]"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Cleansing\n",
    "This section will include all data preparation steps such as:\n",
    "- Handling missing values\n",
    "- Removing duplicates\n",
    "- Data type conversions\n",
    "- Feature engineering\n",
    "- Filtering by year (Post 2010)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values by column:\n",
      "geocoded_city2    39206\n",
      "geocoded_city1    39206\n",
      "fare_low           1612\n",
      "lf_ms              1612\n",
      "carrier_low        1612\n",
      "fare_lg            1540\n",
      "large_ms           1540\n",
      "carrier_lg         1540\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Count total missing values per column\n",
    "missing_summary = df.isnull().sum().sort_values(ascending=False)\n",
    "print(\"Missing values by column:\")\n",
    "print(missing_summary[missing_summary > 0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "geocoded_city2    15.940314\n",
      "geocoded_city1    15.940314\n",
      "fare_low           0.655404\n",
      "lf_ms              0.655404\n",
      "carrier_low        0.655404\n",
      "fare_lg            0.626131\n",
      "large_ms           0.626131\n",
      "carrier_lg         0.626131\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)\n",
    "print(missing_pct[missing_pct > 0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['year', 'quarter', 'city1', 'city2', 'distance', 'passengers', 'fare']\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>distance</th>\n",
       "      <th>passengers</th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>970</td>\n",
       "      <td>180</td>\n",
       "      <td>81.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>970</td>\n",
       "      <td>19</td>\n",
       "      <td>208.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>580</td>\n",
       "      <td>204</td>\n",
       "      <td>184.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>580</td>\n",
       "      <td>264</td>\n",
       "      <td>182.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Phoenix, AZ</td>\n",
       "      <td>328</td>\n",
       "      <td>398</td>\n",
       "      <td>177.11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year  quarter                           city1  \\\n",
       "0  2021        3  Allentown/Bethlehem/Easton, PA   \n",
       "1  2021        3  Allentown/Bethlehem/Easton, PA   \n",
       "2  2021        3                 Albuquerque, NM   \n",
       "3  2021        3                 Albuquerque, NM   \n",
       "4  2021        3                 Albuquerque, NM   \n",
       "\n",
       "                           city2  distance  passengers    fare  \n",
       "0  Tampa, FL (Metropolitan Area)       970         180   81.43  \n",
       "1  Tampa, FL (Metropolitan Area)       970          19  208.93  \n",
       "2          Dallas/Fort Worth, TX       580         204  184.56  \n",
       "3          Dallas/Fort Worth, TX       580         264  182.64  \n",
       "4                    Phoenix, AZ       328         398  177.11  "
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Drop unecessary columns\n",
    "\n",
    "columns_to_drop = [\n",
    "    'geocoded_city1',\n",
    "    'geocoded_city2',\n",
    "    'citymarketid_1',\n",
    "    'citymarketid_2',\n",
    "    'airportid_1',\n",
    "    'airportid_2',\n",
    "    'airport_1',\n",
    "    'airport_2',\n",
    "    'carrier_lg',\n",
    "    'large_ms',\n",
    "    'fare_lg',\n",
    "    'carrier_low',\n",
    "    'fare_low',\n",
    "    'lf_ms',\n",
    "    'tbl1apk'\n",
    "]\n",
    "\n",
    "df = df.drop(columns=columns_to_drop, errors='ignore')\n",
    "\n",
    "#change nsmiles 'column' to 'distance'\n",
    "df = df.rename(columns={'nsmiles': 'distance'})\n",
    "\n",
    "# Preview the dataset\n",
    "print(df.columns.tolist())\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Check for full duplicate rows, Drop full duplicates if any, Check for partial duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of fully duplicated rows: 1\n",
      "Potential partial duplicates based on route and time: 172380\n"
     ]
    }
   ],
   "source": [
    "full_duplicates = df.duplicated()\n",
    "print(f\"Number of fully duplicated rows: {full_duplicates.sum()}\")\n",
    "\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "partial_duplicates = df.duplicated(\n",
    "    subset=['city1', 'city2', 'year', 'quarter']\n",
    ")\n",
    "print(f\"Potential partial duplicates based on route and time: {partial_duplicates.sum()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The dataset contains multiple records per route-quarter, likely representing different carriers or fare observations. Since the analytical grain for this project is route-quarter, records are aggregated prior to modeling to prevent duplicate inflation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    73574.000000\n",
       "mean         3.342947\n",
       "std          2.485533\n",
       "min          1.000000\n",
       "25%          2.000000\n",
       "50%          3.000000\n",
       "75%          4.000000\n",
       "max         33.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['city1','city2','year','quarter']).size().describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Route-quarter observations average ~3.3 records per group, confirming that the raw dataset contains multiple carrier-level entries per route-quarter. Aggregation to the route-quarter level is therefore necessary to avoid duplicate inflation in revenue calculations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>51668</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>1993</td>\n",
       "      <td>4</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51665</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>1993</td>\n",
       "      <td>1</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51669</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>1994</td>\n",
       "      <td>1</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51666</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>1993</td>\n",
       "      <td>2</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51667</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>1993</td>\n",
       "      <td>3</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     city1  \\\n",
       "51668  Los Angeles, CA (Metropolitan Area)   \n",
       "51665  Los Angeles, CA (Metropolitan Area)   \n",
       "51669  Los Angeles, CA (Metropolitan Area)   \n",
       "51666  Los Angeles, CA (Metropolitan Area)   \n",
       "51667  Los Angeles, CA (Metropolitan Area)   \n",
       "\n",
       "                                       city2  year  quarter  count  \n",
       "51668  New York City, NY (Metropolitan Area)  1993        4     33  \n",
       "51665  New York City, NY (Metropolitan Area)  1993        1     33  \n",
       "51669  New York City, NY (Metropolitan Area)  1994        1     33  \n",
       "51666  New York City, NY (Metropolitan Area)  1993        2     32  \n",
       "51667  New York City, NY (Metropolitan Area)  1993        3     32  "
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "route_counts = (\n",
    "    df.groupby(['city1','city2','year','quarter'])\n",
    "      .size()\n",
    "      .reset_index(name='count')\n",
    "      .sort_values('count', ascending=False)\n",
    ")\n",
    "\n",
    "route_counts.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Validation Checks\n",
    "The following checks ensure that key fields fall within expected business constraints before aggregation and modeling."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid Year values: 0 rows\n",
      "Invalid Quarter values: 0 rows\n",
      "Invalid Fare values (≤ 0 or missing): 0 rows\n",
      "Invalid Passenger values (< 0): 0 rows\n",
      "Invalid Distance values: 0 rows\n",
      "Invalid Route records: 0 rows\n"
     ]
    }
   ],
   "source": [
    "def check_invalid(label, condition):\n",
    "    invalid = df[condition]\n",
    "    print(f\"{label}: {len(invalid)} rows\")\n",
    "    return invalid.head()\n",
    "\n",
    "invalid_years = check_invalid(\n",
    "    \"Invalid Year values\",\n",
    "    (df['year'] < 1993) | (df['year'] > 2024)\n",
    ")\n",
    "\n",
    "invalid_quarters = check_invalid(\n",
    "    \"Invalid Quarter values\",\n",
    "    ~df['quarter'].isin([1, 2, 3, 4])\n",
    ")\n",
    "\n",
    "invalid_fares = check_invalid(\n",
    "    \"Invalid Fare values (≤ 0 or missing)\",\n",
    "    (df['fare'] <= 0) | (df['fare'].isna())\n",
    ")\n",
    "\n",
    "invalid_passengers = check_invalid(\n",
    "    \"Invalid Passenger values (< 0)\",\n",
    "    df['passengers'] < 0\n",
    ")\n",
    "\n",
    "invalid_distance = check_invalid(\n",
    "    \"Invalid Distance values\",\n",
    "    (df['distance'] <= 0) | (df['distance'] > 5000)\n",
    ")\n",
    "\n",
    "invalid_routes = check_invalid(\n",
    "    \"Invalid Route records\",\n",
    "    df['city1'].isna() |\n",
    "    df['city2'].isna() |\n",
    "    (df['city1'] == df['city2'])\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No invalid records were identified across year, quarter, fare, passenger volume, distance,or route definitions; therefore, no rows were removed during the data cleaning stage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = ['year','quarter','fare','passengers']\n",
    "df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values after numeric conversion:\n",
      "year          0\n",
      "quarter       0\n",
      "fare          0\n",
      "passengers    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Missing values after numeric conversion:\")\n",
    "print(df[['year','quarter','fare','passengers']].isna().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numeric fields were standardized using pd.to_numeric with coercion to ensure non-numeric values were safely converted to missing values and did not silently corrupt downstream calculations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Removed residual index columns created during previous transformations or CSV exports to ensure clean schema prior to aggregation and modeling."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['year', 'quarter', 'city1', 'city2', 'distance', 'passengers', 'fare']\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 245954 entries, 0 to 245954\n",
      "Data columns (total 7 columns):\n",
      " #   Column      Non-Null Count   Dtype  \n",
      "---  ------      --------------   -----  \n",
      " 0   year        245954 non-null  int64  \n",
      " 1   quarter     245954 non-null  int64  \n",
      " 2   city1       245954 non-null  object \n",
      " 3   city2       245954 non-null  object \n",
      " 4   distance    245954 non-null  int64  \n",
      " 5   passengers  245954 non-null  int64  \n",
      " 6   fare        245954 non-null  float64\n",
      "dtypes: float64(1), int64(4), object(2)\n",
      "memory usage: 15.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df = df.drop(columns=['level_0', 'index'], errors='ignore')\n",
    "\n",
    "print(df.columns.tolist())\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Null Count</th>\n",
       "      <th>Percent Null</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>quarter</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>city1</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>city2</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>distance</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>passengers</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fare</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Null Count  Percent Null\n",
       "year                 0           0.0\n",
       "quarter              0           0.0\n",
       "city1                0           0.0\n",
       "city2                0           0.0\n",
       "distance             0           0.0\n",
       "passengers           0           0.0\n",
       "fare                 0           0.0"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check null counts\n",
    "null_counts = df.isnull().sum()\n",
    "null_pct = (df.isnull().sum() / len(df)) * 100\n",
    "\n",
    "null_summary = pd.DataFrame({\n",
    "    \"Null Count\": null_counts,\n",
    "    \"Percent Null\": null_pct\n",
    "}).sort_values(\"Percent Null\", ascending=False)\n",
    "\n",
    "null_summary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Missing values were evaluated across all columns. Columns with significant missingness (>0) were assessed for relevance before modeling. Core variables (year, quarter, fare, passengers, city1, city2) showed minimal missingness, ensuring model reliability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Year 1994 missing quarters: {2, 3, 4}\n",
      "Year 2024 missing quarters: {2, 3, 4}\n",
      "Number of full years: 29\n",
      "Full years: [1993, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]\n"
     ]
    }
   ],
   "source": [
    "expected_quarters = {1, 2, 3, 4}\n",
    "\n",
    "year_quarter_sets = (\n",
    "    df.groupby('year')['quarter']\n",
    "      .apply(set)\n",
    ")\n",
    "\n",
    "for year, quarters in year_quarter_sets.items():\n",
    "    if quarters != expected_quarters:\n",
    "        print(f\"Year {year} missing quarters: {expected_quarters - quarters}\")\n",
    "\n",
    "full_years = year_quarter_sets[year_quarter_sets.apply(lambda x: x == expected_quarters)]\n",
    "print(\"Number of full years:\", len(full_years))\n",
    "print(\"Full years:\", list(full_years.index))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1993 2024\n",
      "[np.int64(1993), np.int64(1994), np.int64(1996), np.int64(1997), np.int64(1998), np.int64(1999), np.int64(2000), np.int64(2001), np.int64(2002), np.int64(2003)] ... [np.int64(2015), np.int64(2016), np.int64(2017), np.int64(2018), np.int64(2019), np.int64(2020), np.int64(2021), np.int64(2022), np.int64(2023), np.int64(2024)]\n"
     ]
    }
   ],
   "source": [
    "print(df['year'].min(), df['year'].max())\n",
    "print(sorted(df['year'].unique())[:10], '...', sorted(df['year'].unique())[-10:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Full analysis years retained: [np.int64(2010), np.int64(2011), np.int64(2012), np.int64(2013), np.int64(2014), np.int64(2015), np.int64(2016), np.int64(2017), np.int64(2018), np.int64(2019), np.int64(2020), np.int64(2021), np.int64(2022), np.int64(2023)]\n"
     ]
    }
   ],
   "source": [
    "# Remove partial-year data and years not outlined for analysis (e.g., 2024 only contains Q1)\n",
    "# Keep only complete years within the analysis period: 2010–2023\n",
    "# Create cleaned working copy\n",
    "df_clean = df.copy()\n",
    "\n",
    "# Standardize column names\n",
    "df_clean.columns = df_clean.columns.str.strip().str.lower()\n",
    "\n",
    "# Filter to analysis period: 2010–2023\n",
    "df_analysis = df_clean[\n",
    "    (df_clean['year'] >= 2010) &\n",
    "    (df_clean['year'] <= 2023)\n",
    "].copy()\n",
    "\n",
    "# Keep only years with all 4 quarters\n",
    "valid_years = df_analysis.groupby('year')['quarter'].nunique()\n",
    "full_years = valid_years[valid_years == 4].index\n",
    "\n",
    "df_analysis = df_analysis[df_analysis['year'].isin(full_years)].copy()\n",
    "\n",
    "print(\"Full analysis years retained:\", sorted(df_analysis['year'].unique()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['year', 'quarter', 'city1', 'city2', 'distance', 'passengers', 'fare']\n"
     ]
    }
   ],
   "source": [
    "print(df_analysis.columns.tolist())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# To ensure accurate year-over-year and seasonal comparisons, only full years (containing all four quarters) were retained. Partial-year data (e.g., incomplete 2024 records) was excluded to prevent artificial trend distortion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Years retained with all 4 quarters: 2010-2023"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current dataset shape: (112852, 7)\n",
      "Years retained: [np.int64(2010), np.int64(2011), np.int64(2012), np.int64(2013), np.int64(2014), np.int64(2015), np.int64(2016), np.int64(2017), np.int64(2018), np.int64(2019), np.int64(2020), np.int64(2021), np.int64(2022), np.int64(2023)]\n",
      "Unique routes: 912\n"
     ]
    }
   ],
   "source": [
    "# Validate analysis dataset before aggregation\n",
    "print(\"Current dataset shape:\", df_analysis.shape)\n",
    "print(\"Years retained:\", sorted(df_analysis['year'].unique()))\n",
    "print(\"Unique routes:\", df_analysis.groupby(['city1', 'city2']).ngroups)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check raw data grain before route-quarter aggregation\n",
    "group_sizes = df_analysis.groupby(['city1', 'city2', 'year', 'quarter']).size()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max rows in a single route-quarter group: 30\n",
      "\n",
      "Top duplicated route-quarter groups:\n",
      "city1                                city2                                  year  quarter\n",
      "Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)  2014  3          30\n",
      "                                                                            2011  2          30\n",
      "                                                                            2012  4          29\n",
      "                                                                            2010  3          29\n",
      "                                                                            2011  1          29\n",
      "                                                                            2014  1          29\n",
      "                                                                                  2          29\n",
      "                                                                            2011  3          29\n",
      "                                                                            2015  3          29\n",
      "                                                                            2013  2          28\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Max rows in a single route-quarter group:\", group_sizes.max())\n",
    "print(\"\\nTop duplicated route-quarter groups:\")\n",
    "print(group_sizes[group_sizes > 1].sort_values(ascending=False).head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>distance</th>\n",
       "      <th>passengers</th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "      <td>2510</td>\n",
       "      <td>443</td>\n",
       "      <td>264.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "      <td>2510</td>\n",
       "      <td>54</td>\n",
       "      <td>264.17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "      <td>2510</td>\n",
       "      <td>3</td>\n",
       "      <td>311.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "      <td>2510</td>\n",
       "      <td>3</td>\n",
       "      <td>373.38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Los Angeles, CA (Metropolitan Area)</td>\n",
       "      <td>New York City, NY (Metropolitan Area)</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "      <td>2510</td>\n",
       "      <td>86</td>\n",
       "      <td>290.65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 city1                                  city2  \\\n",
       "0  Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)   \n",
       "1  Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)   \n",
       "2  Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)   \n",
       "3  Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)   \n",
       "4  Los Angeles, CA (Metropolitan Area)  New York City, NY (Metropolitan Area)   \n",
       "\n",
       "   year  quarter  distance  passengers    fare  \n",
       "0  2011        2      2510         443  264.11  \n",
       "1  2011        2      2510          54  264.17  \n",
       "2  2011        2      2510           3  311.40  \n",
       "3  2011        2      2510           3  373.38  \n",
       "4  2011        2      2510          86  290.65  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>passengers</th>\n",
       "      <th>fare</th>\n",
       "      <th>distance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>30.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>361.866667</td>\n",
       "      <td>307.373333</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1153.283221</td>\n",
       "      <td>63.576613</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>189.100000</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.500000</td>\n",
       "      <td>266.580000</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>25.500000</td>\n",
       "      <td>297.765000</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>92.000000</td>\n",
       "      <td>332.320000</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6161.000000</td>\n",
       "      <td>489.030000</td>\n",
       "      <td>2510.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        passengers        fare  distance\n",
       "count    30.000000   30.000000      30.0\n",
       "mean    361.866667  307.373333    2510.0\n",
       "std    1153.283221   63.576613       0.0\n",
       "min       0.000000  189.100000    2510.0\n",
       "25%       1.500000  266.580000    2510.0\n",
       "50%      25.500000  297.765000    2510.0\n",
       "75%      92.000000  332.320000    2510.0\n",
       "max    6161.000000  489.030000    2510.0"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "worst_key = group_sizes.idxmax()\n",
    "\n",
    "subset = df_analysis.set_index(['city1','city2','year','quarter']) \\\n",
    "           .loc[[worst_key]] \\\n",
    "           .reset_index()\n",
    "\n",
    "display(subset.head())\n",
    "subset[['passengers','fare','distance']].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most duplicated group: ('Los Angeles, CA (Metropolitan Area)', 'New York City, NY (Metropolitan Area)', np.int64(2011), np.int64(2))\n",
      "Rows in that group: 30\n"
     ]
    }
   ],
   "source": [
    "print(\"Most duplicated group:\", worst_key)\n",
    "print(\"Rows in that group:\", group_sizes.max())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The raw dataset contained multiple observations for the same route-year-quarter. To investigate this, I isolated the most duplicated group and reviewed its underlying records. This confirmed that the source data existed at a more detailed level than route-quarter, so aggregation was required to produce a consistent unit of analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_analysis = df[\n",
    "    (df['year'] >= 2010) &\n",
    "    (df['year'] <= 2023)\n",
    "].copy()\n",
    "\n",
    "# Estimate revenue at the original row level\n",
    "df_analysis['estimated_revenue'] = df_analysis['fare'] * df_analysis['passengers']\n",
    "\n",
    "# Aggregate to route-quarter level\n",
    "route_quarter_agg = (\n",
    "    df_analysis.groupby(['city1', 'city2', 'year', 'quarter'], as_index=False)\n",
    "      .agg(\n",
    "          distance=('distance', 'median'),\n",
    "          total_passengers=('passengers', 'sum'),\n",
    "          estimated_revenue=('estimated_revenue', 'sum')\n",
    "      )\n",
    ")\n",
    "\n",
    "# Calculate passenger-weighted average fare\n",
    "route_quarter_agg['avg_fare'] = (\n",
    "    route_quarter_agg['estimated_revenue'] /\n",
    "    route_quarter_agg['total_passengers']\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I first calculated estimated revenue at the row level by multiplying fare by passengers. I then aggregated the data to the route-quarter level by summing passengers and estimated revenue. Average fare was recalculated as estimated revenue divided by total passengers, creating a passenger-weighted average fare. This same logic was then used to aggregate the data to the route-year level for the final analysis\n",
    "\n",
    "Because the raw dataset includes multiple records per route-quarter (often representing different carriers), fares were aggregated using a passenger-weighted average to avoid bias from unweighted means.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Route-Quarter Aggregation Validation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duplicate route-quarter rows after aggregation: 0\n"
     ]
    }
   ],
   "source": [
    "dupes_quarter = route_quarter_agg.duplicated(subset=['city1','city2','year','quarter']).sum()\n",
    "print(f\"Duplicate route-quarter rows after aggregation: {dupes_quarter}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>distance</th>\n",
       "      <th>total_passengers</th>\n",
       "      <th>estimated_revenue</th>\n",
       "      <th>avg_fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>34746.000000</td>\n",
       "      <td>34746.000000</td>\n",
       "      <td>34746.000000</td>\n",
       "      <td>34746.000000</td>\n",
       "      <td>3.474600e+04</td>\n",
       "      <td>34746.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2016.493237</td>\n",
       "      <td>2.502993</td>\n",
       "      <td>1109.690813</td>\n",
       "      <td>1085.158349</td>\n",
       "      <td>2.303489e+05</td>\n",
       "      <td>221.392516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.026388</td>\n",
       "      <td>1.117840</td>\n",
       "      <td>633.667628</td>\n",
       "      <td>1667.279989</td>\n",
       "      <td>3.575832e+05</td>\n",
       "      <td>59.481484</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>2010.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>148.000000</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>2.020200e+03</td>\n",
       "      <td>72.150000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2013.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>625.000000</td>\n",
       "      <td>273.000000</td>\n",
       "      <td>6.205177e+04</td>\n",
       "      <td>176.356375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2016.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>967.000000</td>\n",
       "      <td>527.000000</td>\n",
       "      <td>1.140913e+05</td>\n",
       "      <td>214.198960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2020.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1501.000000</td>\n",
       "      <td>1167.000000</td>\n",
       "      <td>2.482620e+05</td>\n",
       "      <td>261.213627</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2023.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2724.000000</td>\n",
       "      <td>24735.000000</td>\n",
       "      <td>5.961167e+06</td>\n",
       "      <td>677.121791</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               year       quarter      distance  total_passengers  \\\n",
       "count  34746.000000  34746.000000  34746.000000      34746.000000   \n",
       "mean    2016.493237      2.502993   1109.690813       1085.158349   \n",
       "std        4.026388      1.117840    633.667628       1667.279989   \n",
       "min     2010.000000      1.000000    148.000000         27.000000   \n",
       "25%     2013.000000      2.000000    625.000000        273.000000   \n",
       "50%     2016.000000      3.000000    967.000000        527.000000   \n",
       "75%     2020.000000      4.000000   1501.000000       1167.000000   \n",
       "max     2023.000000      4.000000   2724.000000      24735.000000   \n",
       "\n",
       "       estimated_revenue      avg_fare  \n",
       "count       3.474600e+04  34746.000000  \n",
       "mean        2.303489e+05    221.392516  \n",
       "std         3.575832e+05     59.481484  \n",
       "min         2.020200e+03     72.150000  \n",
       "25%         6.205177e+04    176.356375  \n",
       "50%         1.140913e+05    214.198960  \n",
       "75%         2.482620e+05    261.213627  \n",
       "max         5.961167e+06    677.121791  "
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "route_quarter_agg.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>distance</th>\n",
       "      <th>passengers</th>\n",
       "      <th>fare</th>\n",
       "      <th>estimated_revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>970</td>\n",
       "      <td>180</td>\n",
       "      <td>81.43</td>\n",
       "      <td>14657.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Allentown/Bethlehem/Easton, PA</td>\n",
       "      <td>Tampa, FL (Metropolitan Area)</td>\n",
       "      <td>970</td>\n",
       "      <td>19</td>\n",
       "      <td>208.93</td>\n",
       "      <td>3969.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>580</td>\n",
       "      <td>204</td>\n",
       "      <td>184.56</td>\n",
       "      <td>37650.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Dallas/Fort Worth, TX</td>\n",
       "      <td>580</td>\n",
       "      <td>264</td>\n",
       "      <td>182.64</td>\n",
       "      <td>48216.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>Albuquerque, NM</td>\n",
       "      <td>Phoenix, AZ</td>\n",
       "      <td>328</td>\n",
       "      <td>398</td>\n",
       "      <td>177.11</td>\n",
       "      <td>70489.78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year  quarter                           city1  \\\n",
       "0  2021        3  Allentown/Bethlehem/Easton, PA   \n",
       "1  2021        3  Allentown/Bethlehem/Easton, PA   \n",
       "2  2021        3                 Albuquerque, NM   \n",
       "3  2021        3                 Albuquerque, NM   \n",
       "4  2021        3                 Albuquerque, NM   \n",
       "\n",
       "                           city2  distance  passengers    fare  \\\n",
       "0  Tampa, FL (Metropolitan Area)       970         180   81.43   \n",
       "1  Tampa, FL (Metropolitan Area)       970          19  208.93   \n",
       "2          Dallas/Fort Worth, TX       580         204  184.56   \n",
       "3          Dallas/Fort Worth, TX       580         264  182.64   \n",
       "4                    Phoenix, AZ       328         398  177.11   \n",
       "\n",
       "   estimated_revenue  \n",
       "0           14657.40  \n",
       "1            3969.67  \n",
       "2           37650.24  \n",
       "3           48216.96  \n",
       "4           70489.78  "
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analysis.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>quarter</th>\n",
       "      <th>distance</th>\n",
       "      <th>total_passengers</th>\n",
       "      <th>estimated_revenue</th>\n",
       "      <th>avg_fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>34,746.00</td>\n",
       "      <td>34,746.00</td>\n",
       "      <td>34,746.00</td>\n",
       "      <td>34,746.00</td>\n",
       "      <td>34,746.00</td>\n",
       "      <td>34,746.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2,016.49</td>\n",
       "      <td>2.50</td>\n",
       "      <td>1,109.69</td>\n",
       "      <td>1,085.16</td>\n",
       "      <td>230,348.92</td>\n",
       "      <td>221.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.03</td>\n",
       "      <td>1.12</td>\n",
       "      <td>633.67</td>\n",
       "      <td>1,667.28</td>\n",
       "      <td>357,583.21</td>\n",
       "      <td>59.48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>2,010.00</td>\n",
       "      <td>1.00</td>\n",
       "      <td>148.00</td>\n",
       "      <td>27.00</td>\n",
       "      <td>2,020.20</td>\n",
       "      <td>72.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2,013.00</td>\n",
       "      <td>2.00</td>\n",
       "      <td>625.00</td>\n",
       "      <td>273.00</td>\n",
       "      <td>62,051.77</td>\n",
       "      <td>176.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2,016.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>967.00</td>\n",
       "      <td>527.00</td>\n",
       "      <td>114,091.34</td>\n",
       "      <td>214.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2,020.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>1,501.00</td>\n",
       "      <td>1,167.00</td>\n",
       "      <td>248,261.97</td>\n",
       "      <td>261.21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2,023.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>2,724.00</td>\n",
       "      <td>24,735.00</td>\n",
       "      <td>5,961,167.31</td>\n",
       "      <td>677.12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           year   quarter  distance  total_passengers  estimated_revenue  \\\n",
       "count 34,746.00 34,746.00 34,746.00         34,746.00          34,746.00   \n",
       "mean   2,016.49      2.50  1,109.69          1,085.16         230,348.92   \n",
       "std        4.03      1.12    633.67          1,667.28         357,583.21   \n",
       "min    2,010.00      1.00    148.00             27.00           2,020.20   \n",
       "25%    2,013.00      2.00    625.00            273.00          62,051.77   \n",
       "50%    2,016.00      3.00    967.00            527.00         114,091.34   \n",
       "75%    2,020.00      4.00  1,501.00          1,167.00         248,261.97   \n",
       "max    2,023.00      4.00  2,724.00         24,735.00       5,961,167.31   \n",
       "\n",
       "       avg_fare  \n",
       "count 34,746.00  \n",
       "mean     221.39  \n",
       "std       59.48  \n",
       "min       72.15  \n",
       "25%      176.36  \n",
       "50%      214.20  \n",
       "75%      261.21  \n",
       "max      677.12  "
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.options.display.float_format = '{:,.2f}'.format\n",
    "route_quarter_agg.head()\n",
    "route_quarter_agg.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "route_year_agg = (\n",
    "    route_quarter_agg.groupby(['city1', 'city2', 'year'], as_index=False)\n",
    "    .agg(\n",
    "        distance=('distance', 'median'),\n",
    "        total_passengers=('total_passengers', 'sum'),\n",
    "        estimated_revenue=('estimated_revenue', 'sum')\n",
    "    )\n",
    ")\n",
    "\n",
    "# Calculate passenger-weighted average fare at the yearly level\n",
    "route_year_agg['avg_fare'] = (\n",
    "    route_year_agg['estimated_revenue'] /\n",
    "    route_year_agg['total_passengers']\n",
    ")\n",
    "\n",
    "# Create a readable route name column\n",
    "route_year_agg['route'] = route_year_agg['city1'] + ' → ' + route_year_agg['city2']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I aggregated the route-quarter dataset into route-year level data by summing total passengers and estimated revenue for each route and year. I then recalculated average fare as estimated revenue divided by total passengers so the yearly fare reflects passenger volume. Finally, I created a readable route name by combining the origin and destination city fields."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Route-Year Aggregation Validation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['city1', 'city2', 'year', 'quarter', 'distance', 'total_passengers',\n",
      "       'estimated_revenue', 'avg_fare'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(route_quarter_agg.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "      <th>year</th>\n",
       "      <th>distance</th>\n",
       "      <th>total_passengers</th>\n",
       "      <th>estimated_revenue</th>\n",
       "      <th>avg_fare</th>\n",
       "      <th>route</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Albany, NY</td>\n",
       "      <td>Chicago, IL</td>\n",
       "      <td>2010</td>\n",
       "      <td>723.00</td>\n",
       "      <td>1239</td>\n",
       "      <td>252,144.06</td>\n",
       "      <td>203.51</td>\n",
       "      <td>Albany, NY → Chicago, IL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Albany, NY</td>\n",
       "      <td>Chicago, IL</td>\n",
       "      <td>2011</td>\n",
       "      <td>723.00</td>\n",
       "      <td>1228</td>\n",
       "      <td>273,608.11</td>\n",
       "      <td>222.81</td>\n",
       "      <td>Albany, NY → Chicago, IL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Albany, NY</td>\n",
       "      <td>Chicago, IL</td>\n",
       "      <td>2012</td>\n",
       "      <td>723.00</td>\n",
       "      <td>1207</td>\n",
       "      <td>287,805.90</td>\n",
       "      <td>238.45</td>\n",
       "      <td>Albany, NY → Chicago, IL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Albany, NY</td>\n",
       "      <td>Chicago, IL</td>\n",
       "      <td>2013</td>\n",
       "      <td>723.00</td>\n",
       "      <td>1177</td>\n",
       "      <td>295,396.67</td>\n",
       "      <td>250.97</td>\n",
       "      <td>Albany, NY → Chicago, IL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Albany, NY</td>\n",
       "      <td>Chicago, IL</td>\n",
       "      <td>2014</td>\n",
       "      <td>723.00</td>\n",
       "      <td>1202</td>\n",
       "      <td>311,306.85</td>\n",
       "      <td>258.99</td>\n",
       "      <td>Albany, NY → Chicago, IL</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        city1        city2  year  distance  total_passengers  \\\n",
       "0  Albany, NY  Chicago, IL  2010    723.00              1239   \n",
       "1  Albany, NY  Chicago, IL  2011    723.00              1228   \n",
       "2  Albany, NY  Chicago, IL  2012    723.00              1207   \n",
       "3  Albany, NY  Chicago, IL  2013    723.00              1177   \n",
       "4  Albany, NY  Chicago, IL  2014    723.00              1202   \n",
       "\n",
       "   estimated_revenue  avg_fare                     route  \n",
       "0         252,144.06    203.51  Albany, NY → Chicago, IL  \n",
       "1         273,608.11    222.81  Albany, NY → Chicago, IL  \n",
       "2         287,805.90    238.45  Albany, NY → Chicago, IL  \n",
       "3         295,396.67    250.97  Albany, NY → Chicago, IL  \n",
       "4         311,306.85    258.99  Albany, NY → Chicago, IL  "
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "route_year_agg.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duplicate route-year rows after aggregation: 0\n"
     ]
    }
   ],
   "source": [
    "dupes_year = route_year_agg.duplicated(\n",
    "    subset=['city1', 'city2', 'year']\n",
    ").sum()\n",
    "\n",
    "print(f\"Duplicate route-year rows after aggregation: {dupes_year}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count        9,760.00\n",
      "mean       820,051.58\n",
      "std      1,354,082.39\n",
      "min          2,020.20\n",
      "50%        395,264.42\n",
      "90%      2,036,603.80\n",
      "95%      2,940,845.10\n",
      "99%      5,896,607.45\n",
      "max     21,002,064.48\n",
      "Name: estimated_revenue, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(route_year_agg['estimated_revenue'].describe(percentiles=[0.5,0.9,0.95,0.99]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2010, np.float64(0.4305665505726799)),\n",
       " (2011, np.float64(0.4303278395007025)),\n",
       " (2012, np.float64(0.4294064204149233)),\n",
       " (2013, np.float64(0.4345510902860453)),\n",
       " (2014, np.float64(0.4357092707359858)),\n",
       " (2015, np.float64(0.434863241893964)),\n",
       " (2016, np.float64(0.43304698304387834)),\n",
       " (2017, np.float64(0.43031976336841826)),\n",
       " (2018, np.float64(0.42766855192620784)),\n",
       " (2019, np.float64(0.42665439898452223))]"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top10_share_by_year = []\n",
    "\n",
    "for year, group in route_quarter_agg.groupby('year'):\n",
    "    group_sorted = group.sort_values('estimated_revenue', ascending=False)\n",
    "    cutoff = int(len(group_sorted) * 0.1)\n",
    "    \n",
    "    share = (\n",
    "        group_sorted.iloc[:cutoff]['estimated_revenue'].sum()\n",
    "        / group_sorted['estimated_revenue'].sum()\n",
    "    )\n",
    "    \n",
    "    top10_share_by_year.append((year, share))\n",
    "\n",
    "top10_share_by_year[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I calculated the annual revenue concentration by identifying the top 10% highest-revenue route-quarter observations within each year. For each year, I sorted route-quarters by estimated revenue, summed the estimated revenue from the top 10%, and divided it by total estimated revenue for that year. This shows how much yearly revenue is driven by the highest-performing route-quarters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['city1', 'city2', 'year', 'quarter', 'distance', 'total_passengers', 'estimated_revenue', 'avg_fare']\n"
     ]
    }
   ],
   "source": [
    "print(route_quarter_agg.columns.tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAjt9JREFUeJzs3XmczfX////7MfswcxjMZpmhkJ0QQ9nGNlmSSqIJSUqR0ELvGkrIO1FJWmQJ0Ua2psZa3kyWGiF8VBSZMWI2jJkxXr8/+s3r2zEzzBznzDHcrpfLudTr+Xq+nq/H6+W8zjmPeT5fz5fFMAxDAAAAAADA4cq4OgAAAAAAAK5XJN0AAAAAADgJSTcAAAAAAE5C0g0AAAAAgJOQdAMAAAAA4CQk3QAAAAAAOAlJNwAAAAAATkLSDQAAAACAk5B0AwAAAADgJCTdwDVg/vz5slgs5svd3V0hISHq16+fDh065PT9T548WStWrHDqPvbv369BgwapevXq8vLyUuXKldWjRw99++23Tt1vUSxZskQzZ84s0X0OGjTI5t/c09NTN910k8aOHav09PQSjaU0CQ8PV48ePRzSlsVi0ZNPPlngus8//1wWi0WbNm0yyyZMmCCLxWLXvvKu8Z07d16xbvv27dW+fXu79lOYrKwszZo1S7fffrsqVKggT09PValSRX379tXmzZsduq9rxezZszV//nyntH3u3DlNmDDB5v3hKJs2bcr33itI3nvqyJEjDtt3Yd8FxXn/2is8PNzmM7Gwl7P+Tf9t9erVeuihh9SwYUN5eHhc9rrPycnRxIkTFR4eLi8vL91yyy16++2389X77rvv1LRpU/n5+alt27b65Zdf8tV54okn1K5dOxmG4dDjkaS3335bN998szw9PWWxWJSamlpgvRvh9wjgCiTdwDVk3rx52rZtm9atW6cnn3xSK1eu1O23366UlBSn7tfZX3JffvmlmjZtqu3bt+vFF19UXFycZs+erYsXL6pr16568cUXnbbvonBF0i1JPj4+2rZtm7Zt26aVK1eqQ4cOmj59uu69994SjwVX9sgjj2jbtm2uDqPY/v77b7Vp00ajR49WgwYNNH/+fK1fv17Tp0+Xm5ubIiMjtXv3bleH6XDOTronTpzolKS7qLp3765t27YpJCTEYW26MuFZvny5+Xm4bds2DRkyRJIUGxtrU969e/cSiSU+Pl716tVT48aNL1t3+PDhmjJlip544gl98803uvvuu/XUU09p8uTJZp3U1FTdfffdatGihb788ktZrVb16dNHubm5Zp34+Hh99NFHeu+99+z+415hEhISNHLkSHXo0EEbNmzQtm3b5Ofnd9ltrtffI4CruLs6AAD/T4MGDdS8eXNJ//R25ebmKiYmRitWrNDgwYNdHJ19fvvtN0VHR6thw4batGmTypYta66777779Pjjj2vSpEm69dZbdffdd5dobOfOnZOvr6/T2s/MzJSPj0+h68uUKaNWrVqZy926ddPvv/+uuLg4HT58WDVq1HBabCi+qlWrqmrVqq4Oo9geeugh7d69W9988406duxos65fv34aPXq0KlSo4KLorg05OTlmr15pUblyZVWuXNnVYThM06ZNbZZjY2MlSc2aNVOlSpVKNJYPPvhAZcr80y/15JNPateuXQXW27dvn+bOnatXX31VzzzzjKR/vrtPnTqlSZMm6bHHHlNAQIC2bdumrKwsvfPOO/Lw8FD9+vVVpUoVHTp0SLfccotycnL06KOP6rnnntMtt9zi8OPZt2+fJGno0KG67bbbirTN9fh7BHAlerqBa1jeF96JEydsyleuXKmIiAj5+vrKz89PnTt3ztcDN2jQIIWHh+dr89IhshaLRWfPntWCBQvM4WT/HtqalJSkYcOGqWrVqvL09FSNGjU0ceJEXbhwoUjHMGPGDJ07d05vv/22TcKdZ/r06SpfvrxeeeWVQmPMU9BwymXLlqlLly4KCQmRj4+P6tatq+eff15nz57Ndz7KlSunPXv2qEuXLvLz81NkZKTat2+vNWvW6I8//rAZUpcnOztbkyZN0i233GIOix88eLBOnjxp037esOe8Xn1vb29NnDixSOfo3wr7N1+2bJkiIiJUtmxZlStXTl27dtVPP/1krp85c6YsFot+/fXXfG0+99xz8vT01N9//22WrVu3TpGRkfL395evr6/atGmj9evX22yX9++wb98+PfDAA7JarQoKCtLDDz+stLQ0s96RI0cKHfZpsVg0YcIEm7JDhw6pf//+CgwMlJeXl+rWrat33nmnyOfoUu+++64aN26scuXKyc/PT7fccovGjx9vd3uFKeh9mZWVpTFjxig4OFi+vr5q27atdu3apfDwcA0aNChfGxkZGXr88cdVqVIl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wzh8+LAhyZg3b16+45RkxMTEmMtdu3Y1qlataqSlpdnUe/LJJw1vb2/j9OnTlzttRlhYmNG9e3eb7cqXL3/ZbQoj6YqvjRs3mvUvfV/u27fPkGQ899xzNu3mvW/+fU3lvXeHDx9uU3fatGmGJCMxMdEsa9eundGuXTtzOT093fDz8zOeeuopm23r1atndOjQ4bLH+NhjjxmSjAMHDlzhbPyjX79+hpeXl/Hnn3/alEdFRRm+vr5GamqqYRiGsXHjRkOSceedd9rU+/TTTw1JxrZt2wzD+Od96u/vb9x+++3m+6Ugt9xyi9G0aVPzsy5Pjx49jJCQEPM9XZzzWL9+fZvzmCcv9rZt217hbBjGhQsXjJycHCMyMtK4++67zfKTJ0/me2/nKep7/LnnnjMsFouRkJBgU69z58753nsFKejzsF27doYk44cffrCpW69ePaNr165XPN7CvguKet6L83l1JXnX28mTJw3DMIzY2NgCP4+WLVtmSDLef/99sywsLKzQc+vv72+cPXu2yHE88cQTBX4f5bVXp06dAtd5enoajz76qLk8e/Zsw9PT05BkWK1W46uvvjIMwzA6depkDBkypMjx5ElJSTF8fHzyXYN//vmn4eXlZfTv398sy/v3y/uOvZzS/nvkar4TAGeipxu4hrRq1UoeHh7y8/NTt27dVKFCBX311VfmfYYHDx7U8ePHFR0dbTP8rVy5crrnnnsUHx+vc+fOOSye1atXq0OHDgoNDbXpBYyKipIkc9bj3Nxcu3oJ8xj//0yt9kwe8/vvv6t///4KDg6Wm5ubPDw81K5dO0myGWKXpzi9z6tXr1b58uXVs2dPm+Nr0qSJgoOD802i1KhRI5tegCs5e/asPDw85OHhoUqVKunxxx/X/fffr1dffdWs88033+jChQt66KGHbGLw9vZWu3btbGIYPHiwjh07pnXr1pll8+bNU3BwsPlvtnXrVp0+fVoDBw7M92/WrVs37dixI1+PQK9evfId5/nz54s9MuH8+fNav3697r77bvn6+trs/84779T58+cVHx9frDZvu+02paam6oEHHtBXX31lM4S+KPr27asdO3bke7322mtX3Dbv/d+3b1+b8nvvvbfQe4MLOpeS9McffxS6Hz8/Pw0ePFjz5883/202bNigX3755ap7RS+1YcMGRUZGqlq1ajblgwYN0rlz5/ING73S8WzdulXp6ekaPnx4odf3r7/+qgMHDmjAgAGSlO99kZiYmG/Iuj3n8VKFfRbMmTNHt956q7y9veXu7i4PDw+tX7++wM+TSxXnPb5x40bVr18/30Rd/fv3L/IxFCQ4ODjffbuNGjUq1rkpzJXOe3E+r4prw4YNkpRvaPR9992nsmXL5hulU9i5TU9P148//mh3HJe63PfWv9c9/vjjOn36tPbv368TJ06oV69e+vjjj/Xzzz/rv//9r06fPq0BAwaocuXKuummmzRnzpzL7nfbtm3KzMzMdz6qVaumjh07FjhqqThK6++Rq/1OAJyFpBu4hixcuFA7duzQhg0bNGzYMO3fv18PPPCAuf7UqVOSVOBstaGhobp48aJDZxY9ceKEVq1aZSaGea/69etLkvllFhkZabP+4YcfNtuoXr26OSytMHn3JF76Q/9Kzpw5ozvuuEM//PCDJk2apE2bNmnHjh368ssvJSnf8G9fX1/5+/sXuf0TJ04oNTVVnp6e+c5BUlJSvi/z4s4i7OPjYyZ5q1atUvv27fXJJ59o6tSpNjFI/9x3e2kMy5Yts4khKipKISEhmjdvniQpJSVFK1eu1EMPPSQ3Nzeb9u6999587b322msyDMMcYpunYsWKNst5QyAvPb9XcurUKV24cEFvv/12vn3feeedklTsH0jR0dH66KOP9Mcff+iee+5RYGCgWrZsqbi4uCJtX7lyZTVv3jzf69/D+y93PJIUFBRkU+7u7p7vnOWx91yOGDFCGRkZWrx4sSRp1qxZqlq1qu66667Lbpd3r/aVrsE8p06dKvTzJW/9v13pePLmPrjcBHR578mxY8fme18MHz5cUv73hSPekwUd5xtvvKHHH39cLVu21BdffKH4+Hjt2LFD3bp1K1LbxXmPnzp1Kt+wZEkFlhVHQe89Ly+vYl+vRWn70vNenM+r4jp16pTc3d3zTR5nsVgUHByc7715uXN7aV17VaxYscC2zp49q+zsbAUEBNiUly1b1pwf5NSpUxozZoxmzpypChUq6KmnntLp06f166+/aunSpRo7dqw2btxY6L6v9Hvgao+xtP4eudrvBMBZSs80ncANoG7duuZkJR06dFBubq4+/PBDff7557r33nvNHzyJiYn5tj1+/LjKlCljzkLs7e2d7x43qXhJTaVKldSoUSObntd/y/sh/t57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rHfffffpkUcekSS98soriouL09tvv63Zs2fbtd+kpCRJUlBQkE15UFCQ/vjjD0lS165d9eCDD6pFixby8fHRggULVLZsWT3++OOaP3++3n33Xb399tuqVKmS3n//fdWvX7/Afb366qvq16+fJk6caJY1bty4yLFWrlxZklSxYkUFBweb5a+//rqee+459evXT5L02muvaePGjZo5c6beeecdBQcHy93dXeXKlTO3K1euXL4yZyDpBgAAAHBdyTh/QUnp569YL6S8d76yU2ezi7RtxvkLdsV2Ofv379ejjz5qU9amTZt893lHRETkW7ZnYrFLXfpMasMwbMomTJhgMwR7woQJ6tSpkzw8PDRp0iTt2bNHq1ev1kMPPaRdu3YVuI+EhAQNHTr0qmP9t/T0dB0/flxt2rSxKW/Tpo12797t0H3Zg6QbAAAAwHXFz9tdwf75E+pLVSzrWWBZUbb183ZOKnWlxLeo2xVHXi9vUlKSQkJCzPLk5OR8vd95Dhw4oMWLF+unn37SRx99pLZt26py5crq27evHn74YaWnp8vf3z/fdj4+Plc8DsMwbMpycnKKdBz2njtnI+kGAABAqdfz7S06mZGlyn5eWjXidleHAxd75I6adg/9vnS4eUmqW7eutmzZooceesgs27p1q+rWrWtTLz4+3qZOfHy8mjZtavd+a9SooeDgYMXFxZntZGdna/PmzXrttdfy1TcMQ48++qimT5+ucuXKKTc310yM8/578eLFAvfVqFEjrV+/XoMHDy5wfeXKlZWYmGguHzp0SOfOnTOXPT3/+UNJbm6uWebv76/Q0FBt2bJFbdu2Ncu3bt2q2267rUjnwJlIugEAAFDqnczIKtKQYOBa9swzz6hv37669dZbFRkZqVWrVunLL7/UunXrbOp99tlnat68uW6//XYtXrxY27dv19y5cwtt98yZM/r111/N5cOHDyshIcF85rbFYtGoUaM0efJk1apVS7Vq1dLkyZPl6+ur/v3752vvgw8+UGBgoHr16iXpn2HcEyZMUHx8vL7++mvVq1dP5cuXLzCWmJgYRUZG6qabblK/fv104cIFff3113r22WclSR07dtSsWbPUqlUrXbx4Uc8995w8PDzM7QMDA+Xj46PY2FhVrVpV3t7eslqteuaZZxQTE6ObbrpJTZo00bx585SQkKDFixcX+fw7C0k3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71ZSUpIqV64sNzc3JSYmKjAw8Kp2HhUVpaioqMvW8fLyUnBwcIHr0tLSNHfuXH388cfq1KmTJGnRokWqVq2a1q1bp65du2r//v2KjY1VfHy8WrZsKUn64IMPFBERoYMHD6pOnTpXdQwAAAAAABSmyD3dlStXVnx8vCSZz+MuCZs2bVJgYKBq166toUOHKjk52Vy3a9cu5eTkqEuXLmZZaGioGjRooK1bt0qStm3bJqvVaibcktSqVStZrVazDgAAAAAAzlDknu7HHntMd911l3lvdWG9z5JshnZfjaioKN13330KCwvT4cOH9eKLL6pjx47atWuXvLy8lJSUJE9PT1WoUMFmu6CgICUlJUmSkpKSCuyRDwwMNOsUJCsrS1lZWeZyenq6Q44JAAAAjlejUln5eburUjkvV4cCADaKnHRPmDBB/fr106+//qpevXpp3rx5Kl++vBNDk+6//37z/xs0aKDmzZsrLCxMa9asUZ8+fQrd7tKe+IJ65a/UWz9lyhRNnDjRzsgBAABQkj55tNWVKwGACxQ56ZakW265RbfccotiYmJ03333ydfX11lxFSgkJERhYWE6dOiQJCk4OFjZ2dlKSUmx6e1OTk5W69atzTonTpzI19bJkycVFBRU6L7GjRun0aNHm8vp6emqVq2aow4FAACgVAp/fk2J7u/I1O4luj8AcDS7HhkWExMjX19fnTx5Ulu2bNH//vc/nTx50tGx5XPq1CkdPXpUISEhkqRmzZrJw8NDcXFxZp3ExETt3bvXTLojIiKUlpam7du3m3V++OEHpaWlmXUK4uXlJX9/f5sXAAAAAADFUaye7jznzp3Tk08+qY8//ti8f9vNzU0PPfSQ3n777SL3gJ85c0a//vqruXz48GElJCQoICBAAQEBmjBhgu655x6FhIToyJEjGj9+vCpVqqS7775bkmS1WjVkyBCNGTNGFStWVEBAgMaOHauGDRuas5nXrVtX3bp109ChQ/Xee+9Jkh599FH16NGDmcsBAAAAAE5lV0/3008/rc2bN2vlypVKTU1VamqqvvrqK23evFljxowpcjs7d+5U06ZN1bRpU0nS6NGj1bRpU7300ktyc3PTnj17dNddd6l27doaOHCgateurW3btsnPz89sY8aMGerdu7f69u2rNm3ayNfXV6tWrZKbm5tZZ/HixWrYsKG6dOmiLl26qFGjRvr444/tOXQAAABcg55a+pOi5/6gp5b+5OpQAMCGxTAMo7gbVapUSZ9//rnat29vU75x40b17du3RIaal7T09HRZrValpaUx1BwAVPL3dQJASeE+cgBFUdQc0a6e7nPnzhU4CVlgYKDOnTtnT5MAAAAAAFx37Eq6IyIiFBMTo/Pnz5tlmZmZmjhxoiIiIhwWHAAAAAAApZldE6m9+eab6tatm6pWrarGjRvLYrEoISFB3t7e+uabbxwdIwAAAAAApZJdSXeDBg106NAhLVq0SAcOHJBhGOrXr58GDBggHx8fR8cIAAAAAECpZFfSLUk+Pj4aOnSoI2MBAAAAAOC6Ytc93QAAAAAA4MpIugEAAAAAcBKSbgAAAAAAnISkGwAAAAAAJ7Er6a5Zs6ZOnTqVrzw1NVU1a9a86qAAAAAAALge2JV0HzlyRLm5ufnKs7Ky9Ndff111UAAAAAAAXA+K9ciwlStXmv//zTffyGq1msu5ublav369wsPDHRYcAAAAAAClWbGS7t69e0uSLBaLBg4caLPOw8ND4eHhmj59usOCAwAAAACgNCtW0n3x4kVJUo0aNbRjxw5VqlTJKUEBAAAAAHA9KFbSnefw4cOOjgMAAAAAgOuOXUm3JK1fv17r169XcnKy2QOe56OPPrrqwAAAAAAAKO3sSronTpyol19+Wc2bN1dISIgsFouj4wIAAAAAoNSzK+meM2eO5s+fr+joaEfHAwAAAADAdcOu53RnZ2erdevWjo4FAAAAAIDril1J9yOPPKIlS5Y4OhYAAAAAAK4rdg0vP3/+vN5//32tW7dOjRo1koeHh836N954wyHBAQAAAABQmtmVdP/8889q0qSJJGnv3r0265hUDQAAAACAf9iVdG/cuNHRcQAAAAAAcN2x655uAAAAAABwZXb1dHfo0OGyw8g3bNhgd0AAAAAAAFwv7Eq68+7nzpOTk6OEhATt3btXAwcOdERcAAAAAACUenYl3TNmzCiwfMKECTpz5sxVBQQAAAAAwPXCofd0P/jgg/roo48c2SQAAAAAAKWWQ5Pubdu2ydvb25FNAgAAAABQatk1vLxPnz42y4ZhKDExUTt37tSLL77okMAAAAAAACjt7Eq6rVarzXKZMmVUp04dvfzyy+rSpYtDAgMAAAAAoLSzK+meN2+eo+MAAAAAAOC6Y1fSnWfXrl3av3+/LBaL6tWrp6ZNmzoqLgAAAMAlwp9fU6L7OzK1e4nuD0DJsivpTk5OVr9+/bRp0yaVL19ehmEoLS1NHTp00NKlS1W5cmVHxwkAAAAAQKlj1+zlI0aMUHp6uvbt26fTp08rJSVFe/fuVXp6ukaOHOnoGAEAAAAAKJXs6umOjY3VunXrVLduXbOsXr16euedd5hIDQAAAACA/59dPd0XL16Uh4dHvnIPDw9dvHjxqoMCAAAAAOB6YFfS3bFjRz311FM6fvy4WfbXX3/p6aefVmRkpMOCAwAAAACgNLMr6Z41a5YyMjIUHh6um266STfffLNq1KihjIwMvf32246OEQAAAACAUsmue7qrVaumH3/8UXFxcTpw4IAMw1C9evXUqVMnR8cHAAAAAECpdVXP6e7cubM6d+7sqFgAAAAAALiuFGt4+YYNG1SvXj2lp6fnW5eWlqb69evr+++/d1hwAAAAAACUZsVKumfOnKmhQ4fK398/3zqr1aphw4bpjTfecFhwAAAAAACUZsVKunfv3q1u3boVur5Lly7atWvXVQcFAAAAAMD1oFhJ94kTJwp8Pnced3d3nTx58qqDAgAAAADgelCspLtKlSras2dPoet//vlnhYSEXHVQAAAAAABcD4qVdN9555166aWXdP78+XzrMjMzFRMTox49ejgsOAAAAAAASrNiPTLsP//5j7788kvVrl1bTz75pOrUqSOLxaL9+/frnXfeUW5url544QVnxQoAAAAAQKlSrJ7uoKAgbd26VQ0aNNC4ceN09913q3fv3ho/frwaNGig//3vfwoKCipye99995169uyp0NBQWSwWrVixwma9YRiaMGGCQkND5ePjo/bt22vfvn02dbKysjRixAhVqlRJZcuWVa9evXTs2DGbOikpKYqOjpbVapXValV0dLRSU1OLc+gAAAAAABRbsZJuSQoLC9PatWv1999/64cfflB8fLz+/vtvrV27VuHh4cVq6+zZs2rcuLFmzZpV4Ppp06bpjTfe0KxZs7Rjxw4FBwerc+fOysjIMOuMGjVKy5cv19KlS7VlyxadOXNGPXr0UG5urlmnf//+SkhIUGxsrGJjY5WQkKDo6OjiHjoAAAAAAMViMQzDcHUQkmSxWLR8+XL17t1b0j+93KGhoRo1apSee+45Sf/0agcFBem1117TsGHDlJaWpsqVK+vj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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Comparing top 10% revenue routes vs. bottom 90%\n",
    "p90 = route_quarter_agg['estimated_revenue'].quantile(0.90)\n",
    "\n",
    "plt.close('all')\n",
    "\n",
    "plt.figure(figsize=(10,6))\n",
    "\n",
    "# Histogram\n",
    "plt.hist(\n",
    "    route_quarter_agg['estimated_revenue'],\n",
    "    bins=np.logspace(\n",
    "        np.log10(route_quarter_agg['estimated_revenue'].min()),\n",
    "        np.log10(route_quarter_agg['estimated_revenue'].max()),\n",
    "        30\n",
    "    )\n",
    ")\n",
    "plt.xscale('log')\n",
    "\n",
    "# 90th Percentile cut line\n",
    "plt.axvline(p90, linestyle='--', linewidth=2, label='Top 10% cutoff')\n",
    "\n",
    "plt.title('Route-Quarter Revenue Is Highly Concentrated in the Top 10% of Routes')\n",
    "plt.xlabel('Estimated Revenue per Route per Quarter (log USD)')\n",
    "plt.ylabel('Count of Route-Quarter Observations')\n",
    "plt.legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Route-level revenue is highly concentrated: most routes generate modest quarterly revenue,while the top 10% of routes dominate overall revenue generation. This pattern indicates that airline profitability depends heavily on a small number of consistently high-performing routes. The top 10% of route-quarters account for approximately 45% of total estimated revenue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [],
   "source": [
    "route_year_agg['revenue_decile'] = (\n",
    "    route_year_agg\n",
    "    .groupby('year')['estimated_revenue']\n",
    "    .transform(lambda x: pd.qcut(x, 10, labels=False, duplicates='drop') + 1)\n",
    ")\n",
    "\n",
    "route_year_agg['route_performance_group'] = route_year_agg['revenue_decile'].apply(\n",
    "    lambda x: 'Bottom 10%' if x == 1 else 'Top 10%' if x == 10 else 'Middle 80%'\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I created revenue deciles to rank route-year observations by estimated revenue. This allowed me to compare the highest-performing 10% of routes against the lowest-performing 10% and identify whether revenue differences were driven more by passenger demand, fare levels, or distance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       4\n",
      "1       4\n",
      "2       4\n",
      "3       4\n",
      "4       4\n",
      "       ..\n",
      "9755    8\n",
      "9756    8\n",
      "9757    7\n",
      "9758    8\n",
      "9759    1\n",
      "Name: revenue_decile, Length: 9760, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(route_year_agg['revenue_decile'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.90   2,036,603.80\n",
       "0.95   2,940,845.10\n",
       "0.99   5,896,607.45\n",
       "Name: estimated_revenue, dtype: float64"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "route_year_agg['estimated_revenue'].quantile([0.90, 0.95, 0.99])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34746"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(route_quarter_agg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['city1', 'city2', 'year', 'distance', 'total_passengers', 'estimated_revenue', 'avg_fare', 'route', 'revenue_decile', 'route_performance_group']\n",
      "(9760, 10)\n",
      "        city1        city2  year  distance  total_passengers  \\\n",
      "0  Albany, NY  Chicago, IL  2010    723.00              1239   \n",
      "1  Albany, NY  Chicago, IL  2011    723.00              1228   \n",
      "2  Albany, NY  Chicago, IL  2012    723.00              1207   \n",
      "3  Albany, NY  Chicago, IL  2013    723.00              1177   \n",
      "4  Albany, NY  Chicago, IL  2014    723.00              1202   \n",
      "\n",
      "   estimated_revenue  avg_fare                     route  revenue_decile  \\\n",
      "0         252,144.06    203.51  Albany, NY → Chicago, IL               4   \n",
      "1         273,608.11    222.81  Albany, NY → Chicago, IL               4   \n",
      "2         287,805.90    238.45  Albany, NY → Chicago, IL               4   \n",
      "3         295,396.67    250.97  Albany, NY → Chicago, IL               4   \n",
      "4         311,306.85    258.99  Albany, NY → Chicago, IL               4   \n",
      "\n",
      "  route_performance_group  \n",
      "0              Middle 80%  \n",
      "1              Middle 80%  \n",
      "2              Middle 80%  \n",
      "3              Middle 80%  \n",
      "4              Middle 80%  \n"
     ]
    }
   ],
   "source": [
    "print(route_year_agg.columns.tolist())\n",
    "print(route_year_agg.shape)\n",
    "print(route_year_agg.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9760\n"
     ]
    }
   ],
   "source": [
    "print(len(route_year_agg))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "route_quarter_agg.to_csv(\"route_quarter_agg_tableau.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [],
   "source": [
    "route_year_agg.to_csv(\"route_year_agg_tableau.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/emjack5/Desktop/Data analysis/Capstone2 files\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# To better understand what separates high-revenue routes from the broader market, the Tableau analysis compares the top 10% of routes against the remaining 90% across passenger volume, average fare, and distance. This helps identify whether revenue performance is driven more by demand, pricing, or route characteristics."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Analysis Focus Areas in Tableau\n",
    "\n",
    "The following issues are derived from the capstone issue tree:\n",
    "\n",
    "1. **Route Revenue Trends**\n",
    "   - Which routes generate the highest estimated revenue?\n",
    "   - How concentrated is revenue among the top-performing routes?\n",
    "     \n",
    "2.  **Drivers of Revenue**\n",
    "   - Do high-revenue routes have higher passenger volume, higher fares, or longer distances?\n",
    "   - What differentiates top 10% routes from lower-performing routes?\n",
    "\n",
    "3. **Performance Over Time**\n",
    "   - How did passenger volume, average fare, and estimated revenue change from 2010 to 2023?\n",
    "   - How did major disruptions, such as COVID-19, affect route performance?\n",
    "\n",
    "4. **Strategic Recommendations**\n",
    "   - Which route characteristics should airlines prioritize?\n",
    "   - Should airlines focus more on increasing demand, adjusting fares, or reallocating service?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Assumptions & Limitations\n",
    "\n",
    "- Estimated revenue is calculated as fare × passengers.\n",
    "- No cost, margin, or operating expense data is included, so this analysis does not measure true profitability.\n",
    "- Analysis is limited to complete full-year observations from 2010 to 2023.\n",
    "- Routes are defined as directional city pairs using city1 → city2.\n",
    "- Revenue performance is evaluated at the route-year level for final analysis."
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python [conda env:base]",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
