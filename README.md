# Bikeshare Data Analysis (Udacity fork)

This repository is a **fork** of the Udacity bikeshare project. It analyzes US bikeshare usage data and prints key statistics about travel times, stations, trip durations, and user types.  
It works **interactively** in the terminal and reads one of three CSV datasets:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

---

## Project structure

```
.
├── bikeshedding.py        # Entry point (interactive CLI)
└── README.md
```

The script follows the classic Udacity structure with functions like `get_filters()`, `load_data()`, `time_stats()`, `station_stats()`, `trip_duration_stats()`, and `user_stats()`.
It asks you for a **city**, **month** (`all`, `january`…`june`), and **day of week** (`all`, `monday`…`sunday`) and then prints the computed statistics. It also offers to display raw data in chunks.

---

## Quickstart

### 1) Clone **your fork**
```bash
git clone https://github.com/<your-username>/<your-fork>.git
cd <your-fork>
```

### 2) (Optional) Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3) Install dependencies
This project only needs **pandas** and **numpy** in addition to Python 3.
```bash
python -m pip install --upgrade pip
pip install pandas numpy
```

### 4) Add datasets
Place `chicago.csv`, `new_york_city.csv`, and `washington.csv` in the repository root (next to `bikeshedding.py`).  
If you store them elsewhere, update the `CITY_DATA` mapping in `bikeshedding.py` accordingly.

### 5) Run
```bash
python bikeshedding.py
```

Follow the prompts, e.g.
```
Hello! Let's explore some US bikeshare data!
Which city? [chicago, new york city, washington]:
Which month? [all, january, february, march, april, may, june]:
Which day?   [all, monday, tuesday, wednesday, thursday, friday, saturday, sunday]:
```

---

## Troubleshooting

- **File not found**: Make sure the CSV filenames match exactly (including underscores) and are in the expected location.
- **Non‑UTF8 errors on Windows**: Run `chcp 65001` in CMD first or use PowerShell.
- **Pandas too old**: Upgrade via `pip install -U pandas`.

---

## How to use (developer notes)

- The entrypoint is `bikeshedding.py`. The `CITY_DATA` dict maps lowercase city names to CSV paths.
- The script converts `Start Time` to `datetime` and derives `month` and `day_of_week` columns for filtering.
- Month/day filters accept the strings listed in the `months` and `days` lists in the script.
- The statistics functions print summaries to stdout; no files are written.

If you want non‑interactive execution, a simple extension is to parse command‑line args (`argparse`) and bypass `input()`—but the default behavior is interactive.

---

## Contribution guidelines

This is a personal fork used to complete the Udacity project. PRs are welcome for:
- Code clarity and comments
- Small bug fixes
- Portability improvements (e.g., argument parsing)

Please open an issue first if proposing larger changes. Keep the dataset filenames and columns compatible with the Udacity CSVs.

---

## Credits

- Upstream project by **Udacity** (Data Analyst Nanodegree bikeshare project).  
- CSV datasets provided by Udacity as part of the coursework.
- ChatGPT for this beautiful README.md

---

## License

This fork **inherits the license** of the upstream repository. See the `LICENSE` file in the original Udacity repo. If you add a local `LICENSE`, state clearly that it mirrors upstream.

---

## Date created

2025-10-24
