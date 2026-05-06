from datetime import datetime
import pytz
import tzlocal   

# ===== LẤY GIỜ THEO MÚI GIỜ CHỌN =====
def get_time_by_timezone(tz_name):
    try:
        tz = pytz.timezone(tz_name)
        return datetime.now(tz)
    except:
        # fallback nếu sai timezone
        return datetime.now()

# ===== LẤY GIỜ ĐỊA PHƯƠNG =====
def get_local_time():
    try:
        tz = tzlocal.get_localzone()  
        return datetime.now(tz)
    except:
        # fallback nếu lỗi
        return datetime.now()

# ===== FORMAT HIỂN THỊ =====
def format_time(dt, show_seconds=True):
    if show_seconds:
        return dt.strftime("%H:%M:%S - %d/%m/%Y")
    else:
        return dt.strftime("%H:%M - %d/%m/%Y")