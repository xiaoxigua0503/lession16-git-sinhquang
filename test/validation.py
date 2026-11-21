from datetime import date

def is_valid_date_range(start_date:str, end_date:str) -> bool:    
    start_date=date.fromisoformat(start_date)
    end_date=date.fromisoformat(end_date)
    return start_date > end_date

print(is_valid_date_range("2023-01-01", "2023-12-31")) 