from flask import Flask, redirect, render_template_string
import os

app = Flask(__name__)

REDIRECT_URL = 'https://t.me/+0wsZAVlDft80M2Q1'
OG_TITLE = '진짜 중요합니다 주식장 큰일났어요'
OG_DESC = '시간 없습니다 정보는 지금 바로 올릴게요'
OG_IMAGE = 'https://i.ibb.co/BYpL01V/image.jpg'

PAGE = f'''<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta property="og:title" content="{OG_TITLE}">
<meta property="og:description" content="{OG_DESC}">
<meta property="og:image" content="{OG_IMAGE}">
<meta http-equiv="refresh" content="1; url={REDIRECT_URL}">
<title>{OG_TITLE}</title>
</head><body style="font-family:sans-serif;text-align:center;padding:50px;">
<h2>{OG_TITLE}</h2>
<p>{OG_DESC}</p>
<p>잠시만 기다려주세요...</p>
<script>setTimeout(()=>location.href="{REDIRECT_URL}",1000);</script>
</body></html>'''

@app.route('/')
def home():
    return render_template_string(PAGE)

if name == 'main':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
