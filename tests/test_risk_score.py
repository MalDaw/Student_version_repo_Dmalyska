import pytest
from risk_score import calculate_risk_score

# --- TESTY POPRAWNYCH OBLICZEŃ (HAPPY PATH) ---

@pytest.mark.parametrize("age, chol, hr, expected", [
    (50, 200, 150, 15.5),  # Standardowy przypadek
    (52, 240, 150, 17.9),  # Standardowy przypadek
    (20, 100, 180, 3.6),   # Młoda osoba
    (80, 300, 120, 27.4),  # Starsza osoba
    (30, 25, 200, 1.25),   # Niskie ryzyko (blisko granicy cholesterolu)
    (40, 50, 250, 3.0),    # Bardzo wysokie tętno (wynik dodatni)
    (20, 20, 250, 0.0),    # Wynik ujemny w teorii, ale funkcja powinna zwrócić 0.0
])
def test_calculate_risk_score_valid_cases(age, chol, hr, expected):
    assert calculate_risk_score(age, chol, hr) == expected

# --- TESTY BŁĘDÓW TYPÓW (TYPEERROR) ---

@pytest.mark.parametrize("age, chol, hr, invalid_param_name", [
    ('50', 200, 150, 'age'),
    (50, None, 150, 'cholesterol'),
    (50, 200, [150], 'max_heart_rate'),
])
def test_calculate_risk_score_invalid_types(age, chol, hr, invalid_param_name):
    # Test nazwania błędnego parametru
    with pytest.raises(TypeError, match=f"Parametr '{invalid_param_name}' musi być liczbą"):
        calculate_risk_score(age, chol, hr)

# --- TESTY REALISTYCZNYCH ZAKRESÓW (VALUEERROR) ---

@pytest.mark.parametrize("age, chol, hr, match_msg", [
    # Wiek
    (0, 200, 150, "Wiek 0 jest poza realistycznym zakresem"),
    (121, 200, 150, "Wiek 121 jest poza realistycznym zakresem"),
    # Cholesterol
    (50, 15, 150, "Poziom cholesterolu 15 jest poza zakresem"),
    (50, 601, 150, "Poziom cholesterolu 601 jest poza zakresem"),
    # Tętno
    (50, 200, 20, "Tętno 20 jest poza fizjologicznym zakresem"),
    (50, 200, 300, "Tętno 300 jest poza fizjologicznym zakresem"),
])
def test_calculate_risk_score_out_of_range(age, chol, hr, match_msg):
    with pytest.raises(ValueError, match=match_msg):
        calculate_risk_score(age, chol, hr)

# --- TESTY WARTOŚCI BRZEGOWYCH ---

def test_calculate_risk_score_returns_float():
    result = calculate_risk_score(50, 200, 150)
    assert isinstance(result, float)

def test_calculate_risk_score_boundary_values():
    # Sprawdzenie wartości granicznych, które powinny jeszcze przejść
    assert calculate_risk_score(120, 600, 250) == 46.5
    assert calculate_risk_score(1, 20, 30) == 0.3