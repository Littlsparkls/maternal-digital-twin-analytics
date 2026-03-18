{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def detect_twin_shifts(df, window=7, sigma=2.0):\n",
    "    \"\"\"\n",
    "    Core logic for N-of-1 shift detection.\n",
    "    \"\"\"\n",
    "    df['true_baseline_mu'] = df.groupby('Patient_ID')['SystolicBP'].transform(lambda x: x.iloc[:30].mean())\n",
    "    df['true_baseline_std'] = df.groupby('Patient_ID')['SystolicBP'].transform(lambda x: x.iloc[:30].std())\n",
    "    df['current_mu'] = df.groupby('Patient_ID')['SystolicBP'].transform(lambda x: x.rolling(window).mean())\n",
    "    df['is_anomaly'] = df['current_mu'] > (df['true_baseline_mu'] + (sigma * df['true_baseline_std']))\n",
    "    return df\n"
   ]
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
   "version": "3.13.1+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
