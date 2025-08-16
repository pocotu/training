"""
Solution for Time Converter
Problem ID: F069
"""

def seconds_to_hms(seconds):
    """
    Converts seconds to hours:minutes:seconds format.
    Args:
        seconds (int): total seconds
    Returns:
        str: time in HH:MM:SS format
    """
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def hms_to_seconds(time_str):
    """
    Converts HH:MM:SS format to total seconds.
    Args:
        time_str (str): time in HH:MM:SS format
    Returns:
        int: total seconds
    """
    parts = time_str.split(":")
    if len(parts) != 3:
        return 0
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        return 0

def add_time(time1, time2):
    """
    Adds two time strings.
    Args:
        time1 (str): first time in HH:MM:SS
        time2 (str): second time in HH:MM:SS
    Returns:
        str: sum of times in HH:MM:SS
    """
    seconds1 = hms_to_seconds(time1)
    seconds2 = hms_to_seconds(time2)
    total_seconds = seconds1 + seconds2
    
    return seconds_to_hms(total_seconds)

def main():
    """
    Función principal para 069_time_converter
    """
    # Ejemplos de uso
    print("Seconds to HMS:")
    test_seconds = [3661, 7200, 90, 0]
    for sec in test_seconds:
        hms = seconds_to_hms(sec)
        print(f"{sec} seconds = {hms}")
    
    print("\nHMS to Seconds:")
    test_times = ["01:01:01", "02:00:00", "00:01:30", "00:00:00"]
    for time_str in test_times:
        sec = hms_to_seconds(time_str)
        print(f"{time_str} = {sec} seconds")
    
    print("\nAdd Times:")
    time_pairs = [("01:30:00", "00:45:30"), ("00:30:30", "01:40:45")]
    for t1, t2 in time_pairs:
        result = add_time(t1, t2)
        print(f"{t1} + {t2} = {result}")
    
    return seconds_to_hms(3661)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")
