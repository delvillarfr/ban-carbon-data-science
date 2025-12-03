# Revenue Forecast

Grassroots donation revenue forecasting for BAN CARBON.

## Overview

This project implements the revenue forecasting methodology described in:
`/home/fdvom/ban-carbon-hq/research/revenue-forecast/context/forecasting-methodology.md`

The forecast calculates M-month revenue based on:
- **Channels**: Ways to reach potential donors
- **Segments**: Donor groups with shared characteristics
- **Funnel metrics**: Audience size, lead rates, conversion rates
- **Donor behavior**: Gift amounts and attrition rates

## Structure

```
revenue-forecast/
├── notebooks/         # Analysis notebook
│   └── 1-revenue-forecast.ipynb
└── README.md
```

Data is located at repository root:
```
../../data/raw/revenue-forecasts/
├── channels.csv
├── segments.csv
├── structural-parameters.csv
├── audience-size/
│   ├── chatgpt.csv
│   ├── claude.csv
│   └── gemini.csv
├── lead-rates/
│   └── combined.csv
└── gift-amounts/
    └── combined.csv
```

## Usage

1. Open and run `notebooks/1-revenue-forecast.ipynb`
2. Review forecasted revenue and breakdowns

## Revenue Formula

```
revenue = Σ_c Σ_s [ n_cs × lead_c × conv × Σ_{t=m_c}^M gift_s × (1 - attr)^{t - m_c} ]
```

Where:
- `n_cs`: Reachable audience in segment s via channel c
- `lead_c`: Channel c lead rate
- `conv`: Lead-to-donor conversion rate
- `gift_s`: Average monthly gift from segment s
- `attr`: Monthly attrition rate
- `m_c`: Month when channel c is activated
- `M`: Forecast horizon (months)

## Input Tables

CSV files in `../../data/raw/revenue-forecasts/`:

1. **channels.csv**: `id_c`, `name_c`, `description_c`
2. **segments.csv**: `id_s`, `name_s`, `description_s`
3. **lead-rates/combined.csv**: `id_c`, `lead`
4. **gift-amounts/combined.csv**: `id_s`, `gift`
5. **audience-size/{chatgpt,claude,gemini}.csv**: `id_c`, `id_s`, `n`
6. **structural-parameters.csv**: `conv`, `attr`
