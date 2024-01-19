{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ed9c05a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4f7306d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"D:\\\\jyotsna\\\\python folder\\\\placement.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8ddf2b4f",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8.14</td>\n",
       "      <td>6.52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.17</td>\n",
       "      <td>5.17</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.88</td>\n",
       "      <td>7.27</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.52</td>\n",
       "      <td>7.30</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cgpa  resume_score  placed\n",
       "0  8.14          6.52       1\n",
       "1  6.17          5.17       0\n",
       "2  8.27          8.86       1\n",
       "3  6.88          7.27       1\n",
       "4  7.52          7.30       1"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7261f454",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>6.33</td>\n",
       "      <td>6.38</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>8.23</td>\n",
       "      <td>7.76</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>6.65</td>\n",
       "      <td>7.78</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>8.14</td>\n",
       "      <td>5.63</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>6.09</td>\n",
       "      <td>6.61</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "95  6.33          6.38       0\n",
       "96  8.23          7.76       1\n",
       "97  6.65          7.78       0\n",
       "98  8.14          5.63       1\n",
       "99  6.09          6.61       0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "41ad18f1",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100.0000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>6.9422</td>\n",
       "      <td>6.930500</td>\n",
       "      <td>0.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.1192</td>\n",
       "      <td>0.979608</td>\n",
       "      <td>0.502519</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>5.2700</td>\n",
       "      <td>4.950000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>5.9800</td>\n",
       "      <td>6.190000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>6.6200</td>\n",
       "      <td>7.055000</td>\n",
       "      <td>0.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>8.0450</td>\n",
       "      <td>7.640000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.4000</td>\n",
       "      <td>9.060000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           cgpa  resume_score      placed\n",
       "count  100.0000    100.000000  100.000000\n",
       "mean     6.9422      6.930500    0.500000\n",
       "std      1.1192      0.979608    0.502519\n",
       "min      5.2700      4.950000    0.000000\n",
       "25%      5.9800      6.190000    0.000000\n",
       "50%      6.6200      7.055000    0.500000\n",
       "75%      8.0450      7.640000    1.000000\n",
       "max      9.4000      9.060000    1.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df.describe() #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2031ec1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    8.27\n",
       "3    6.88\n",
       "4    7.52\n",
       "5    8.77\n",
       "Name: cgpa, dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[2:5 , \"cgpa\"] #last index is added"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6a09fa8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    8.27\n",
       "3    6.88\n",
       "Name: cgpa, dtype: float64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2:4 , 0]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1384c23c",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.88</td>\n",
       "      <td>7.27</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.52</td>\n",
       "      <td>7.30</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cgpa  resume_score  placed\n",
       "2  8.27          8.86       1\n",
       "3  6.88          7.27       1\n",
       "4  7.52          7.30       1"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[2:4 , :]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6ebc8a0c",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.88</td>\n",
       "      <td>7.27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cgpa  resume_score\n",
       "2  8.27          8.86\n",
       "3  6.88          7.27"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2:4 , 0:2]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a1d4197a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    8.27\n",
       "3    6.88\n",
       "Name: cgpa, dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2:4 , 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c4ca5a1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "top_left_corner_df = df.iloc[:4 , :3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ee2db666",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8.14</td>\n",
       "      <td>6.52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.17</td>\n",
       "      <td>5.17</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.88</td>\n",
       "      <td>7.27</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cgpa  resume_score  placed\n",
       "0  8.14          6.52       1\n",
       "1  6.17          5.17       0\n",
       "2  8.27          8.86       1\n",
       "3  6.88          7.27       1"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_left_corner_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "46106d79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[RangeIndex(start=0, stop=100, step=1),\n",
       " Index(['cgpa', 'resume_score', 'placed'], dtype='object')]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.axes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6247bdd3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cgpa            float64\n",
       "resume_score    float64\n",
       "placed            int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8de30029",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.empty  # if there is no entryin dataframe then its output will be true otherwise false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b581aba2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100, 3)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c4d882cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[8.14, 6.52, 1.  ],\n",
       "       [6.17, 5.17, 0.  ],\n",
       "       [8.27, 8.86, 1.  ],\n",
       "       [6.88, 7.27, 1.  ],\n",
       "       [7.52, 7.3 , 1.  ],\n",
       "       [8.77, 6.19, 1.  ],\n",
       "       [5.34, 7.09, 0.  ],\n",
       "       [6.56, 6.29, 0.  ],\n",
       "       [6.32, 6.71, 0.  ],\n",
       "       [7.69, 7.12, 1.  ],\n",
       "       [6.18, 6.35, 0.  ],\n",
       "       [5.44, 6.54, 0.  ],\n",
       "       [6.09, 7.01, 0.  ],\n",
       "       [8.5 , 5.09, 1.  ],\n",
       "       [7.51, 6.25, 1.  ],\n",
       "       [8.88, 5.93, 1.  ],\n",
       "       [8.04, 7.64, 1.  ],\n",
       "       [7.81, 8.71, 1.  ],\n",
       "       [5.94, 5.88, 0.  ],\n",
       "       [6.75, 8.11, 1.  ],\n",
       "       [5.8 , 8.06, 0.  ],\n",
       "       [6.53, 7.64, 0.  ],\n",
       "       [6.16, 5.77, 0.  ],\n",
       "       [6.05, 7.13, 0.  ],\n",
       "       [8.22, 6.18, 1.  ],\n",
       "       [7.76, 5.68, 1.  ],\n",
       "       [6.27, 6.47, 0.  ],\n",
       "       [5.51, 6.15, 0.  ],\n",
       "       [7.46, 7.67, 1.  ],\n",
       "       [6.19, 7.3 , 0.  ],\n",
       "       [7.36, 7.15, 1.  ],\n",
       "       [5.92, 7.02, 0.  ],\n",
       "       [5.87, 7.96, 0.  ],\n",
       "       [8.43, 7.73, 1.  ],\n",
       "       [8.87, 7.19, 1.  ],\n",
       "       [8.07, 7.48, 1.  ],\n",
       "       [8.16, 7.56, 1.  ],\n",
       "       [9.05, 8.21, 1.  ],\n",
       "       [6.  , 8.72, 0.  ],\n",
       "       [7.5 , 6.19, 1.  ],\n",
       "       [8.25, 5.32, 1.  ],\n",
       "       [8.68, 5.15, 1.  ],\n",
       "       [6.9 , 6.91, 1.  ],\n",
       "       [8.21, 7.95, 1.  ],\n",
       "       [5.47, 5.92, 0.  ],\n",
       "       [8.1 , 5.44, 1.  ],\n",
       "       [5.83, 5.21, 0.  ],\n",
       "       [7.05, 8.14, 1.  ],\n",
       "       [5.54, 6.57, 0.  ],\n",
       "       [5.46, 6.73, 0.  ],\n",
       "       [8.22, 6.74, 1.  ],\n",
       "       [6.54, 7.39, 0.  ],\n",
       "       [5.9 , 7.5 , 0.  ],\n",
       "       [6.  , 7.16, 0.  ],\n",
       "       [5.92, 7.18, 0.  ],\n",
       "       [6.94, 6.87, 1.  ],\n",
       "       [6.13, 6.43, 0.  ],\n",
       "       [6.34, 7.21, 0.  ],\n",
       "       [6.47, 7.37, 0.  ],\n",
       "       [5.95, 7.57, 0.  ],\n",
       "       [5.87, 6.64, 0.  ],\n",
       "       [6.89, 7.96, 1.  ],\n",
       "       [5.75, 8.43, 0.  ],\n",
       "       [8.65, 7.58, 1.  ],\n",
       "       [7.93, 8.09, 1.  ],\n",
       "       [6.04, 8.75, 0.  ],\n",
       "       [8.35, 8.02, 1.  ],\n",
       "       [6.59, 6.81, 1.  ],\n",
       "       [6.01, 7.49, 0.  ],\n",
       "       [8.06, 9.06, 1.  ],\n",
       "       [7.12, 7.41, 1.  ],\n",
       "       [7.34, 8.22, 1.  ],\n",
       "       [7.63, 7.98, 1.  ],\n",
       "       [5.76, 6.48, 0.  ],\n",
       "       [5.54, 7.36, 0.  ],\n",
       "       [6.34, 7.94, 1.  ],\n",
       "       [9.4 , 5.5 , 1.  ],\n",
       "       [5.88, 6.92, 0.  ],\n",
       "       [5.79, 5.66, 0.  ],\n",
       "       [5.27, 7.28, 0.  ],\n",
       "       [7.83, 7.7 , 1.  ],\n",
       "       [6.12, 6.72, 0.  ],\n",
       "       [7.92, 6.06, 1.  ],\n",
       "       [7.6 , 8.08, 1.  ],\n",
       "       [5.76, 6.49, 0.  ],\n",
       "       [6.72, 5.46, 0.  ],\n",
       "       [6.18, 5.76, 0.  ],\n",
       "       [5.62, 5.05, 0.  ],\n",
       "       [8.07, 6.07, 1.  ],\n",
       "       [5.99, 7.49, 0.  ],\n",
       "       [5.85, 5.56, 0.  ],\n",
       "       [8.28, 6.3 , 1.  ],\n",
       "       [5.43, 6.18, 0.  ],\n",
       "       [9.31, 7.39, 1.  ],\n",
       "       [8.01, 4.95, 1.  ],\n",
       "       [6.33, 6.38, 0.  ],\n",
       "       [8.23, 7.76, 1.  ],\n",
       "       [6.65, 7.78, 0.  ],\n",
       "       [8.14, 5.63, 1.  ],\n",
       "       [6.09, 6.61, 0.  ]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "085f66a4",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>8.01</td>\n",
       "      <td>4.95</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87</th>\n",
       "      <td>5.62</td>\n",
       "      <td>5.05</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>8.50</td>\n",
       "      <td>5.09</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>8.68</td>\n",
       "      <td>5.15</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.17</td>\n",
       "      <td>5.17</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>7.81</td>\n",
       "      <td>8.71</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>6.00</td>\n",
       "      <td>8.72</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>6.04</td>\n",
       "      <td>8.75</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>8.06</td>\n",
       "      <td>9.06</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "94  8.01          4.95       1\n",
       "87  5.62          5.05       0\n",
       "13  8.50          5.09       1\n",
       "41  8.68          5.15       1\n",
       "1   6.17          5.17       0\n",
       "..   ...           ...     ...\n",
       "17  7.81          8.71       1\n",
       "38  6.00          8.72       0\n",
       "65  6.04          8.75       0\n",
       "2   8.27          8.86       1\n",
       "69  8.06          9.06       1\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values(by = \"resume_score\") # sort function retuen asending number by default"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "79ea50d9",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8.14</td>\n",
       "      <td>6.52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.17</td>\n",
       "      <td>5.17</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.27</td>\n",
       "      <td>8.86</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.88</td>\n",
       "      <td>7.27</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.52</td>\n",
       "      <td>7.30</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cgpa  resume_score  placed\n",
       "0  8.14          6.52       1\n",
       "1  6.17          5.17       0\n",
       "2  8.27          8.86       1\n",
       "3  6.88          7.27       1\n",
       "4  7.52          7.30       1"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1b0f5aba",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "0      8             6       1\n",
       "1      6             5       0\n",
       "2      8             8       1\n",
       "3      6             7       1\n",
       "4      7             7       1\n",
       "..   ...           ...     ...\n",
       "95     6             6       0\n",
       "96     8             7       1\n",
       "97     6             7       0\n",
       "98     8             5       1\n",
       "99     6             6       0\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = df.astype(int)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f200a90a",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = x.astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fbe91a3e",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>6.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>8.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>8.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>6.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "0    8.0           6.0     1.0\n",
       "1    6.0           5.0     0.0\n",
       "2    8.0           8.0     1.0\n",
       "3    6.0           7.0     1.0\n",
       "4    7.0           7.0     1.0\n",
       "..   ...           ...     ...\n",
       "95   6.0           6.0     0.0\n",
       "96   8.0           7.0     1.0\n",
       "97   6.0           7.0     0.0\n",
       "98   8.0           5.0     1.0\n",
       "99   6.0           6.0     0.0\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "891a11a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b9d20727",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "0      8             6       1\n",
       "1      6             5       0\n",
       "2      8             8       1\n",
       "3      6             7       1\n",
       "4      7             7       1\n",
       "..   ...           ...     ...\n",
       "95     6             6       0\n",
       "96     8             7       1\n",
       "97     6             7       0\n",
       "98     8             5       1\n",
       "99     6             6       0\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "da931621",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     8.0\n",
       "1     6.0\n",
       "2     8.0\n",
       "3     6.0\n",
       "4     7.0\n",
       "     ... \n",
       "95    6.0\n",
       "96    8.0\n",
       "97    6.0\n",
       "98    8.0\n",
       "99    6.0\n",
       "Name: cgpa, Length: 100, dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x['cgpa']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6bd51c6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     6.0\n",
       "1     5.0\n",
       "2     8.0\n",
       "3     7.0\n",
       "4     7.0\n",
       "     ... \n",
       "95    6.0\n",
       "96    7.0\n",
       "97    7.0\n",
       "98    5.0\n",
       "99    6.0\n",
       "Name: resume_score, Length: 100, dtype: float64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x['resume_score']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e2146b80",
   "metadata": {},
   "outputs": [],
   "source": [
    "x['cgpa'] = x['cgpa'].add(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d75ec7c2",
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
       "      <th>cgpa</th>\n",
       "      <th>resume_score</th>\n",
       "      <th>placed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>10.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>12.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>10.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>12.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>10.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    cgpa  resume_score  placed\n",
       "0   12.0           6.0     1.0\n",
       "1   10.0           5.0     0.0\n",
       "2   12.0           8.0     1.0\n",
       "3   10.0           7.0     1.0\n",
       "4   11.0           7.0     1.0\n",
       "..   ...           ...     ...\n",
       "95  10.0           6.0     0.0\n",
       "96  12.0           7.0     1.0\n",
       "97  10.0           7.0     0.0\n",
       "98  12.0           5.0     1.0\n",
       "99  10.0           6.0     0.0\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "67c5f134",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cgpa            100\n",
       "resume_score    100\n",
       "placed          100\n",
       "dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "94601098",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cgpa            9\n",
       "resume_score    9\n",
       "placed          1\n",
       "dtype: int32"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5472f47c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cgpa            5\n",
       "resume_score    4\n",
       "placed          0\n",
       "dtype: int32"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c91c4095",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
