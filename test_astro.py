import math
import ephem
from PIL import Image

# 1. Sənin verdiyin mükəmməl kordinatlar
merkez_x = 1126
merkez_y = 1250
radius = 500

print("Astroloji hesablamalar aparılır...")

# 2. Şablonu açırıq
img = Image.open('sablon.png').convert('RGBA')

# 3. İkonları açırıq və ölçüsünü dizayna uyğunlaşdırırıq (məsələn 80x80 piksel)
# .convert("RGBA") arxa planın tam şəffaf qalmasını təmin edir
gunes_ikon = Image.open('gunes.png').convert("RGBA")
gunes_ikon = gunes_ikon.resize((80, 80))

ay_ikon = Image.open('ay.png').convert("RGBA")
ay_ikon = ay_ikon.resize((80, 80))

# ==========================================
# 4. MÜŞTƏRİNİN MƏLUMATLARI (Buranı dəyişib test edə bilərsən)
# Format: 'İl/Ay/Gün Saat:Dəqiqə'
# ==========================================
tarix = '1995/10/15 14:30'

# ephem ilə səmadakı planetləri tapırıq
gunes = ephem.Sun(tarix)
ay = ephem.Moon(tarix)

# 5. Dərəcəni Kordinata Çevirən Sehrli Funksiya
def kordinati_tap(planet_obyekti):
    # Planetin səmada neçə dərəcədə olduğunu tapırıq (0-360 dərəcə arası)
    ecl = ephem.Ecliptic(ephem.Equatorial(planet_obyekti.a_ra, planet_obyekti.a_dec))
    astro_derece = math.degrees(ecl.lon)
    
    # Sənin dizaynına uyğunlaşdırmaq üçün riyazi çevirmə (Qoç bürcü solda olduğu üçün)
    riyazi_bucaq = math.radians(180 - astro_derece)
    
    # Sinus və Kosinus ilə mərkəzdən radius qədər kənara çıxırıq
    x = merkez_x + radius * math.cos(riyazi_bucaq)
    y = merkez_y - radius * math.sin(riyazi_bucaq)
    
    return int(x), int(y)

# 6. Günəş və Ayın tam yerləşəcəyi x və y nöqtələrini alırıq
gx, gy = kordinati_tap(gunes)
ax, ay_y = kordinati_tap(ay)

# 7. İkonları şəklin üzərinə yapışdırırıq!
# (İkonun tam mərkəzə düşməsi üçün x və y-dən ikonun yarısını, yəni 40 px çıxırıq)
img.paste(gunes_ikon, (gx - 40, gy - 40), gunes_ikon)
img.paste(ay_ikon, (ax - 40, ay_y - 40), ay_ikon)

# 8. Nəticəni yaddaşa veririk
img.save('hazir_xarite.png')
print("✅ Möhtəşəm! Astroloji xəritə hazırlandı və 'hazir_xarite.png' olaraq yaddaşa verildi!")