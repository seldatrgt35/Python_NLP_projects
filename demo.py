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
    f"📢 Özel Fırsat! 📢\n"
    f"Bakiye kontrolünü elden bırakma! Bugün en yakın restoranlardan birinde yemek yersen **%10 indirim** senin!\n"
    f"Multipay ayrıcalıklarıyla avantajları yakala! 🍽️\n"
    f"📍 Uygulamayı kontrol et ve fırsatları kaçırma!"
)

@app.route('/')
def index():
    return render_template('index.html', user=low_balance_user, campaign=campaign_message)

@app.route('/approve_campaign', methods=['POST'])
def approve_campaign():
    return jsonify({"status": "success", "message": "Kampanya onaylandı ve müşteriye gönderildi!"})

if __name__ == '__main__':
    app.run(debug=True)
