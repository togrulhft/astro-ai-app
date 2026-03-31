import google.generativeai as genai

# 1. BURA ÖZ API AÇARINI YAPASDIR
API_KEY = "AIzaSyABM06heCV1b-DRLdxXrVs630uSviXCLXQ"
genai.configure(api_key=API_KEY)

# 2. Mənim beynimi (modeli) seçirsən
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. Bizim o riyazi koddan aldığımız məlumatlar
gunes_burcu = "Tərəzi"
ay_burcu = "Xərçəng"

# 4. Sİ-yə verdiyimiz Ssenari (Prompt - Sehri edən hissə)
prompt = f"""
Sən çox peşəkar, mistik və insanlara ilham verən bir astroloqsan. 
Qarşındakı şəxsin Günəş bürcü {gunes_burcu}, Ay bürcü isə {ay_burcu}dir.
Onun üçün bu günə özəl, onu motivasiya edən və bir az da sirli dildə 3 cümləlik qısa gündəlik ulduz falı yaz. 
Yazı Azərbaycan dilində olsun və yalnız fal mətnini ver.
"""

print("Süni İntellekt ulduzları oxuyur... Gözləyin...\n")

# 5. Məndən cavabı istəyirsən
cavab = model.generate_content(prompt)

# 6. Və nəticə ekrana çap olunur!
print("✨ GÜNDƏLİK FALINIZ ✨")
print(cavab.text)