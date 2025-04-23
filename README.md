# 🤼 WWE Match Outcome Predictor

> Bringing AI to the squared circle — because wrestling analytics just got a whole lot smarter.

---

## 🔥 What Makes This Special

While most sports prediction projects rely on static datasets, **we built our dataset dynamically** using:

### ⚙️ LLM-Powered Web Scraping  
We scraped **live event pages** from [SmackDown Hotel](https://www.thesmackdownhotel.com) — *but instead of writing custom parsers*, we:

- Used **BeautifulSoup** to get raw HTML from WWE event pages.
- Passed that HTML to a **Large Language Model (LLM)** (`google/gemma-2-2b-it`) via **Hugging Face Inference API**.
- Prompted the LLM to extract structured data:
  - `Event Name`, `Match`, `Winner`, `Loser`, and `Title Match`

This let us **automatically convert messy HTML → clean CSV** without writing XPath or Regex logic. That’s futuristic web scraping.

---

## 🧠 ML Pipeline

Once our LLM-fed CSV was ready, we:
- 🧹 Cleaned and standardized wrestler names
- 🔄 Encoded matchups (Player 1 vs Player 2) and randomized order to simulate real-world uncertainty
- 🧮 Trained a **Random Forest Classifier**
- 🔍 Tuned it with **GridSearchCV** for best parameters

---

## 📊 Results

| Metric      | Training | Testing |
|-------------|----------|---------|
| Accuracy    | 100%     | ~61%    |
| F1-Score    | 1.00     | 0.61    |

Not perfect, but solid for a first stab using basic features.

---

## 🎮 Sample Prediction

> Cody Rhodes vs Solo Sikoa at WWE Backlash (Title Match)  
>  
> 🎯 Predicted Winner: Cody Rhodes

---

## 💡 What You Could Build on Top

- A fantasy match simulator
- Real-time predictor using live data
- Add wrestler stats, win streaks, venues, and crowd size
- Deploy as a Streamlit app or Discord bot

---

## 🗂️ Key Files

- `scrape_wwe_events.py` — uses LLMs to turn HTML into gold
- `clean_and_merge.py` — preps and encodes data
- `train_model.py` — Random Forest training
- `wwe_ml_cleaned.csv` — your ready-to-train dataset

---

## 💬 Final Word

> People scrape tables. We scraped **stories**, powered by LLMs.  
> Welcome to the future of wrestling analytics.

🕶️ *Bravo 6, scraping complete.*
