import os
from dotenv import load_dotenv
from django.shortcuts import render
from twilio.rest import Client

# Create your views here.
from django.shortcuts import render

load_dotenv()


# Create your views here.
def season(request):
    return render(request, 'pages/season.html')
    
def send_report_via_sms():
    account_sid = os.getenv("ACCOUNT_SID_VIEW")

    auth_token = os.getenv("AUTH_TOKEN_VIEW")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+19893941530',
            body = f'''नमस्ते, शुजा उर रहमान
                    उत्पाद का नाम: मक्का 🌽
                    समाप्ति तिथि: कल, 26-02-2024

                    उत्पाद का नाम: ज्वार 🌱
                    समाप्ति तिथि: कल, 26-02-2024

                    उत्पाद का नाम: गेहूं 🌾
                    समाप्ति तिथि: कल, 26-02-2024

                    उत्पाद का नाम: चावल 🌾
                    समाप्ति तिथि: कल, 26-02-2024

                    कृपया इन्हें जल्द से जल्द उपयोग करें या बाजार में बेचने के लिए विचार करें। धन्यवाद!''',
  to='+918657689680'
    )

    print(message.sid)




def crops(request):
    return render(request, 'pages/crops.html')

def fertilizer(request):
    return render(request, 'pages/fertilizer.html')

def seed(request):
    return render(request, 'pages/seed.html')

def profit(request):
    return render(request, 'pages/profit.html')

def utilized(request):
    return render(request, 'pages/utilized.html')

def table(request):
    return render(request, 'pages/table.html')
