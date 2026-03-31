import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

gunes_burcu = "Tərəzi"
ay_burcu = "Xərçəng"

prompt = f"""
Sən çox peşəkar, mistik və insanlara ilham verən bir astroloqsan. 
Qarşındakı şəxsin Günəş bürcü {gunes_burcu}, Ay bürcü isə {ay_burcu}dir.
Onun üçün bu günə özəl, onu motivasiya edən və bir az da sirli dildə 3 cümləlik qısa gündəlik ulduz falı yaz. 
Yazı Azərbaycan dilində olsun və yalnız fal mətnini ver.
"""

print("Süni İntellekt ulduzları oxuyur... Gözləyin...\n")

cavab = model.generate_content(prompt)


print("✨ GÜNDƏLİK FALINIZ ✨")
print(cavab.text)
