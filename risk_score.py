def calculate_risk_score(age: float, cholesterol: float, max_heart_rate: float) -> float:
    """
    Oblicza wskaźnik ryzyka zdrowotnego na podstawie wieku, cholesterolu i tętna.
    Wynik jest ograniczony do zakresu od 0 wzwyż.
    """
    AGE_WEIGHT = 0.2
    CHOL_WEIGHT = 0.05
    MHR_WEIGHT = 0.03

    params = {'age': age, 'cholesterol': cholesterol, 'max_heart_rate': max_heart_rate}
    for name, value in params.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parametr '{name}' musi być liczbą (obecnie: {type(value).__name__}).")

    if not (0 < age <= 120):
        raise ValueError(f"Wiek {age} jest poza realistycznym zakresem (1-120).")
    
    if not (20 <= cholesterol <= 600):
        raise ValueError(f"Poziom cholesterolu {cholesterol} jest poza zakresem (20-600).")
    
    if not (30 <= max_heart_rate <= 250):
        raise ValueError(f"Tętno {max_heart_rate} jest poza fizjologicznym zakresem (30-250).")

    raw_score = (age * AGE_WEIGHT) + (cholesterol * CHOL_WEIGHT) - (max_heart_rate * MHR_WEIGHT)
    return max(0.0, round(raw_score, 2))