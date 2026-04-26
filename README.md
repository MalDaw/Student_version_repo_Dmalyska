# Laboratorium: AI w pracy inżyniera oprogramowania

To repozytorium jest wersją dla studentów.

## Co będziesz robić
Podczas zajęć wykorzystasz AI do:
- analizy kodu,
- poprawiania błędów,
- pisania testów,
- refaktoryzacji,
- dokumentowania rozwiązania.

## Wymagania
- Python 3.10+
- pytest
- Git
- VS Code lub Visual Studio
- GitHub Copilot lub inne narzędzie AI

## Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Pliki
- `task.md` — instrukcja do wykonania,
- `bad_example.py` — kod z błędem,
- `risk_score.py` — funkcja do testów,
- `analyze_heart_data.py` — skrypt do analizy danych,
- `tests/` — testy,
- `docs/prompts.md` — przykładowe prompty.

## Dane
- Heart CSV: https://raw.githubusercontent.com/plotly/datasets/master/heart.csv
- Breast Cancer sklearn: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html
- UCI Heart Disease: https://archive.ics.uci.edu/dataset/45/heart+disease
