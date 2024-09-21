from datetime import datetime

def formatted_current_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d')
    return formatted_date
