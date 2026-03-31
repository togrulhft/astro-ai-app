import streamlit as st
import ephem
import math
import google.generativeai as genai
from PIL import Image
from datetime import datetime

# --- 1. Sİ və API Ayarları ---
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') # və ya bayaq işləyən ad hansı idisə

# --- 2. Vebsaytın Dizaynı və Başlığı ---
st.set_page_config(page_title="Mistik Astrologiya", page_icon="✨")
st.title("✨ Sizin Süni İntellekt Astroloqunuz")
st.write("Doğum məlumatlarınızı daxil edin və ulduzların sizə nə dediyini öyrənin!")

# İstifadəçidən məlumat alırıq
col1, col2 = st.columns(2)
with col1:
    dogum_tarixi = st.date_input("Doğum Tarixiniz", min_value=datetime(1930, 1, 1))
with col2:
    dogum_saati = st.time_input("Doğum Saatınız (Təxmini)")

# --- 3. SEHİRLİ DÜYMƏ ---
if st.button("🔮 Xəritəmi və Falımı Yarat"):
    
    with st.spinner('Ulduzlar oxunur... Zəhmət olmasa gözləyin...'):
        
        # Tarixi ephem formatına salırıq
        tarix_str = f"{dogum_tarixi.strftime('%Y/%m/%d')} {dogum_saati.strftime('%H:%M')}"
        
        # Astronomik hesablamalar
        gunes = ephem.Sun(tarix_str)
        ay = ephem.Moon(tarix_str)
        
        # Bürclərin adını tapmaq (Sİ-yə vermək üçün)
        gunes_const = ephem.constellation(gunes)[1]
        ay_const = ephem.constellation(ay)[1]
        
        # --- ŞƏKİL YARATMA İŞLƏMİ ---
        merkez_x = 1126
        merkez_y = 1250
        radius = 500
        
        img = Image.open('sablon.png').convert('RGBA')
        gunes_ikon = Image.open('gunes.png').convert("RGBA").resize((80, 80))
        ay_ikon = Image.open('ay.png').convert("RGBA").resize((80, 80))
        
        def kordinati_tap(planet_obyekti):
            ecl = ephem.Ecliptic(ephem.Equatorial(planet_obyekti.a_ra, planet_obyekti.a_dec))
            astro_derece = math.degrees(ecl.lon)
            riyazi_bucaq = math.radians(180 - astro_derece)
            x = merkez_x + radius * math.cos(riyazi_bucaq)
            y = merkez_y - radius * math.sin(riyazi_bucaq)
            return int(x), int(y)
            
        gx, gy = kordinati_tap(gunes)
        ax, ay_y = kordinati_tap(ay)
        
        img.paste(gunes_ikon, (gx - 40, gy - 40), gunes_ikon)
        img.paste(ay_ikon, (ax - 40, ay_y - 40), ay_ikon)
        
       # --- SÜNİ İNTELLEKT FAL İŞLƏMİ ---
        prompt = f"""
        Sən çox peşəkar, dərin bilikləri olan, insanlara yol göstərən və onlara dəyərli məsləhətlər verən bir astroloqsan. 
        Qarşındakı şəxsin Günəş bürcü {gunes_const}, Ay bürcü isə {ay_const} bürcündədir.
        
        Onun üçün bu günə özəl, çox aydın, anlaşıqlı və qısa bir gündəlik ulduz falı yaz. 
        Mətn 3 abzasdan ibarət olsun və aşağıdakı strukturu izləsin:
        
        1-ci abzas (Günün Enerjisi): Günəş və Ay bürcünün bugünkü harmoniyası onun daxili dünyasına, hisslərinə və enerjisinə necə təsir edəcək? Bunu sadə dillə izah et.
        2-ci abzas (Diqqət edilməli məqamlar): Gün ərzində iş, münasibətlər və ya verəcəyi qərarlarda nələrə diqqət etməlidir? Hansı fürsətlər və ya kiçik risklər var?
        3-cü abzas (Motivasiya): Ona güc verən, gününü gözəlləşdirəcək və pozitiv kökləyəcək müdrik, isti bir məsləhətlə yekunlaşdır.
        
        Yazı mütləq səlis, qrammatik cəhətdən doğru və təbii Azərbaycan dilində olsun. Mistik aurasını qorusun, amma oxuyan üçün tam aydın və yolgöstərici olsun. Yalnız fal mətnini yaz, əlavə sözlər (məsələn, "İşte falınız" və s.) istifadə etmə.
        """
        cavab = model.generate_content(prompt)
        
        # --- NƏTİCƏLƏRİ EKRANA ÇIXARMAQ ---
        st.success("Mistik xəritəniz hazırdır!")
        st.image(img, caption="Sizin Fərdi Astroloji Xəritəniz")
        
        st.subheader("✨ Gündəlik Falınız")
        st.write(cavab.text)
        
        st.balloons() # Ekrana şarlar uçururuq!