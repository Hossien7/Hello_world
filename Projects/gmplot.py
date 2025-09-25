# python
import gmplot

# ⚠️ جایگزین کنید: کلید API گوگل مپ خود را اینجا وارد کنید
# Example: api_key = 'AIzaSy...your...key'
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY" 

# مختصات جغرافیایی مورد نظر (مثال: تهران - برج میلاد)
latitude = 35.783611
longitude = 51.378056

# می‌توانید یک لیست از مختصات را نیز برای نمایش چند نقطه تعریف کنید
# latitude_list = [35.783611, 35.788, 35.8]
# longitude_list = [51.378056, 51.385, 51.365]


# ۱. ایجاد یک شیء نقشه (Map Object)
# آرگومان‌ها: عرض مرکزی، طول مرکزی، سطح زوم (۱ تا ۲۲)
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 14, apikey=API_KEY)


# ۲. افزودن نشانگر (Marker) برای نقطه مورد نظر
# رنگ نشانگر را می‌توانید تغییر دهید (مثلاً: '#FF0000' برای قرمز)
gmap.marker(latitude, longitude, color='red', title='Milad Tower - Tehran')

# اگر لیست مختصات داشتید، از gmap.scatter یا gmap.plot استفاده کنید
# gmap.scatter(latitude_list, longitude_list, '#0000FF', size=50, marker=True)


# ۳. ذخیره نقشه در یک فایل HTML
# این فایل را در همان مسیری که کد پایتون را اجرا می‌کنید، ذخیره می‌کند
gmap.draw("my_map.html") 

print("فایل نقشه با نام 'my_map.html' با موفقیت ایجاد شد.")
print("آن را در مرورگر وب خود باز کنید.")