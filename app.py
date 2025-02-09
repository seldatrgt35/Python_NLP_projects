from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# TXT dosyasından veriyi okuma fonksiyonu
def read_txt_data(filename):
    df = pd.read_csv(filename)  # TXT dosyası CSV formatında olduğu için pandas ile okuyabiliyoruz
    return df

# Veriyi txt dosyasından okuma
df = read_txt_data("multipay_data.txt")

# En düşük bakiyeye sahip müşteriyi bulma
low_balance_user = df[df["CardBalance"] == df["CardBalance"].min()].iloc[0]

# AI tarafından oluşturulacak kampanya mesajı
campaign_message = (
    f"📢 Özel Teklif Senin İçin! 📢\n"
    f"Merhaba {low_balance_user['CardNo']}, \n"
    f"Bakiye kontrolünü elden bırakma! \n"
    f"Bugün {low_balance_user['SectorName']} kategorisindeki en iyi fırsatlarla sana özel \n"
    f"**%10 indirim** seni bekliyor! 🎉\n"
    f"📍 Hemen en yakın anlaşmalı işletmeyi keşfet ve avantajı kaçırma!"
)

@app.route('/')
def index():
    return render_template('customer_view.html', user=low_balance_user, campaign=campaign_message)

@app.route('/use_campaign', methods=['POST'])
def use_campaign():
    return jsonify({"status": "success", "message": "Kampanya kullanıldı! İyi alışverişler!"})

if __name__ == '__main__':
    app.run(debug=True)
