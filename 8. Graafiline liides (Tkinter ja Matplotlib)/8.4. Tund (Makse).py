import requests
import json
import webbrowser
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import string
import smtplib
from email.mime.text import MIMEText
#https://support.every-pay.com/merchant-support/testing-open-banking-payments-in-demo-environment/

# EveryPay данные
API_URL = "https://igw-demo.every-pay.com/api/v4/payments/oneoff"
API_AUTH = "ZTM2ZWI0MGY1ZWM4N2ZhMjo3YjkxYTNiOWUxYjc0NTI0YzJlOWZjMjgyZjhhYzhjZA=="
API_USERNAME = "e36eb40f5ec87fa2"
ACCOUNT_NAME = "EUR3D1"
CUSTOMER_URL = "https://maksmine.web.app/makse"

payment_reference = ""  # Глобально для хранения ID платежа


# Генерация nonce
def generate_nonce(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Отправка email после успешной оплаты
def saada_email(to_email, payment_reference):
    sender = "mariia.smolina@gmail.com"
    password = "utnh zlza okne zbps"

    content = f"Tere!\n\nTeie makse (ID: {payment_reference}) õnnestus edukalt.\n\nAitäh!"
    msg = MIMEText(content)
    msg["Subject"] = "Makse kinnitamine"
    msg["From"] = sender
    msg["To"] = to_email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("E-mail saadetud!")
    except Exception as e:
        print("E-maili saatmise viga:", e)


# Логирование платежей
def logi_makse(payment_reference, status):
    with open("maksete_logi.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} - {payment_reference} - {status}\n")


# Проверка статуса платежа
def kontrolli_makset():
    global payment_reference
    if not payment_reference:
        messagebox.showerror("Ошибка", "Сначала нужно создать платёж.")
        return

    status_url = f"https://igw-demo.every-pay.com/api/v4/payments/{payment_reference}?api_username={API_USERNAME}"
    headers = {
        "Authorization": f"Basic {API_AUTH}"
    }
    response = requests.get(status_url, headers=headers)

    if response.status_code == 200:
        makse_info = response.json()
        seisund = makse_info.get("payment_state")
        messagebox.showinfo("Статус платежа", f"Статус: {seisund}")
        logi_makse(payment_reference, seisund)

        if seisund == "settled":
            saada_email("andreiismolin@gmail.com", payment_reference)
    else:
        messagebox.showerror("Ошибка", f"Не удалось проверить платёж: {response.text}")



# Создание платежа
def create_payment():
    global payment_reference
    amount = amount_entry.get().strip()
    if not amount or not amount.replace(".", "", 1).isdigit():
        messagebox.showerror("Ошибка", "Введите корректную сумму")
        return

    data = {
        "api_username": API_USERNAME,
        "account_name": ACCOUNT_NAME,
        "amount": amount,
        "order_reference": str(random.randint(100000, 999999)),
        "nonce": generate_nonce(),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "customer_url": CUSTOMER_URL
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {API_AUTH}"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        payment_info = response.json()
        payment_reference = payment_info["payment_reference"]
        payment_link = payment_info["payment_link"]
        messagebox.showinfo("Оплата", f"Перенаправляем вас на оплату.\nСсылка: {payment_link}")
        webbrowser.open(payment_link)
    else:
        messagebox.showerror("Ошибка", f"Не удалось создать платёж: {response.status_code}\n{response.text}")


# GUI
app = tk.Tk()
app.title("Оплата через EveryPay")
app.geometry("400x300")

tk.Label(app, text="Введите сумму для оплаты:", font=("Arial", 12)).pack(pady=10)

amount_entry = tk.Entry(app, font=("Arial", 14))
amount_entry.pack(pady=5)

pay_button = tk.Button(app, text="Оплатить", font=("Arial", 14), command=create_payment, bg="green", fg="white")
pay_button.pack(pady=10)

status_button = tk.Button(app, text="Проверить статус", font=("Arial", 14), command=kontrolli_makset, bg="blue", fg="white")
status_button.pack(pady=10)

app.mainloop()
