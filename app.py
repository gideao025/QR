from flask import Flask, render_template, request
import qrcode
import os
from datetime import datetime

app = Flask(__name__)

# Pasta para salvar QR codes temporariamente
QR_CODE_DIR = "static/qrcodes"
if not os.path.exists(QR_CODE_DIR):
    os.makedirs(QR_CODE_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    if request.method == "POST":
        # Obtém o texto do formulário
        text = request.form.get("text")
        if text:
            # Gera um nome de arquivo único baseado no timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            qr_filename = f"qrcode_{timestamp}.png"
            qr_path = os.path.join(QR_CODE_DIR, qr_filename)
            
            # Cria o QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            # Gera a imagem do QR codes
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(qr_path)
            
            # Remove QR codes antigos (mantém apenas o mais recente)
            for old_file in os.listdir(QR_CODE_DIR):
                if old_file != qr_filename:
                    os.remove(os.path.join(QR_CODE_DIR, old_file))
            
            qr_image = qr_filename
    
    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)