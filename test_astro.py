import math
import ephem
from PIL import Image

merkez_x = 1126
merkez_y = 1250
radius = 500

print("Astroloji hesablamalar aparılır...")

img = Image.open('sablon.png').convert('RGBA')


gunes_ikon = Image.open('gunes.png').convert("RGBA")
gunes_ikon = gunes_ikon.resize((80, 80))

ay_ikon = Image.open('ay.png').convert("RGBA")
ay_ikon = ay_ikon.resize((80, 80))

# ==========================================
# 
# Format: 'İl/Ay/Gün Saat:Dəqiqə'
# ==========================================
tarix = '1995/10/15 14:30'


gunes = ephem.Sun(tarix)
ay = ephem.Moon(tarix)


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


img.save('hazir_xarite.png')
print("✅ Möhtəşəm! Astroloji xəritə hazırlandı və 'hazir_xarite.png' olaraq yaddaşa verildi!")
