from flask import Flask, render_template
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

# 윤석열 대통령 퇴임일
target_date = datetime(2027, 5, 9, 23, 59, 59, tzinfo=pytz.timezone('Asia/Seoul'))

@app.route('/')
def countdown():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    remaining = target_date - now
    
    years = remaining.days // 365
    months = (remaining.days % 365) // 30
    days = (remaining.days % 365) % 30
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return render_template('countdown.html', years=years, months=months, days=days, 
                           hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)