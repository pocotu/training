"""
Test cases for Time Converter (Problem F069)
"""

import pytest
from solution import seconds_to_hms, hms_to_seconds, add_time

def test_seconds_to_hms():
    """Test conversion from seconds to HH:MM:SS"""
    assert seconds_to_hms(3661) == "01:01:01"
    assert seconds_to_hms(7200) == "02:00:00"
    assert seconds_to_hms(0) == "00:00:00"
    assert seconds_to_hms(59) == "00:00:59"
    assert seconds_to_hms(3600) == "01:00:00"
    assert seconds_to_hms(3665) == "01:01:05"

def test_hms_to_seconds():
    """Test conversion from HH:MM:SS to seconds"""
    assert hms_to_seconds("01:01:01") == 3661
    assert hms_to_seconds("02:00:00") == 7200
    assert hms_to_seconds("00:00:00") == 0
    assert hms_to_seconds("00:00:59") == 59
    assert hms_to_seconds("01:00:00") == 3600
    assert hms_to_seconds("01:01:05") == 3665

def test_add_time():
    """Test time addition"""
    assert add_time("01:30:45", "02:15:30") == "03:46:15"
    assert add_time("23:45:30", "00:30:45") == "24:16:15"
    assert add_time("00:00:30", "00:00:45") == "00:01:15"
    assert add_time("12:59:59", "00:00:01") == "13:00:00"
    assert add_time("01:30:30", "01:30:30") == "03:01:00"

def test_conversions_consistency():
    """Test that conversions are consistent"""
    test_seconds = [0, 59, 3600, 3661, 7200, 43200, 86399]
    
    for seconds in test_seconds:
        hms = seconds_to_hms(seconds)
        back_to_seconds = hms_to_seconds(hms)
        assert back_to_seconds == seconds

def test_time_addition_consistency():
    """Test time addition consistency"""
    # Test that adding times gives the same result as adding seconds
    time1 = "01:15:30"
    time2 = "02:30:45"
    
    # Convert to seconds, add, convert back
    sec1 = hms_to_seconds(time1)
    sec2 = hms_to_seconds(time2)
    total_seconds = sec1 + sec2
    expected = seconds_to_hms(total_seconds)
    
    # Add times directly
    result = add_time(time1, time2)
    
    assert result == expected

def test_edge_cases():
    """Test edge cases"""
    assert seconds_to_hms(86399) == "23:59:59"  # Max seconds in a day - 1
    assert hms_to_seconds("23:59:59") == 86399
    assert add_time("00:00:00", "00:00:00") == "00:00:00"
