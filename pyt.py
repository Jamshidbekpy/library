from apps.books.models import Book  # Modelingizni to'g'ri import qiling
from decimal import Decimal

# Kitob ma'lumotlari (rasmlar Google'dan olingan URL bilan)
books = [
    {"title": "Python Dasturlash Asoslari", "author": "Ali Valiyev", "genre": "Dasturlash", 
     "description": "Python dasturlash tili haqida mukammal qo'llanma.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", 
     "price": Decimal("19.99")},

    {"title": "Ma'lumotlar Ilmi", "author": "Shahzod Karimov", "genre": "Data Science", 
     "description": "Ma'lumotlarni qayta ishlash va tahlil qilish bo'yicha qo'llanma.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/1/18/Data_Science_Venn_Diagram.png", 
     "price": Decimal("24.99")},

    {"title": "Sun'iy Intellekt Asoslari", "author": "Nodirbek Omonov", "genre": "AI", 
     "description": "Sun'iy intellekt haqida boshlang'ich ma'lumot.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg", 
     "price": Decimal("29.99")},

    {"title": "Mashina O'rganish", "author": "Dilnoza Rahimova", "genre": "Machine Learning", 
     "description": "Mashina o'rganish algoritmlari bo'yicha chuqur tushuncha.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Neural_network_example.svg", 
     "price": Decimal("34.99")},

    {"title": "Deep Learning", "author": "Javohir Bekmurodov", "genre": "Deep Learning", 
     "description": "Deep Learning va neyron tarmoqlar bo'yicha qo'llanma.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Deep_Learning.jpg", 
     "price": Decimal("39.99")},

    {"title": "Kiberxavfsizlik", "author": "Rustam Norqobilov", "genre": "Cybersecurity", 
     "description": "Kiberxavfsizlik asoslari va amaliy tajribalar.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Information_Security_Concept_Visualization.png", 
     "price": Decimal("44.99")},

    {"title": "Ma'lumotlar bazasi", "author": "Gulnoza Xudoyberdiyeva", "genre": "Database", 
     "description": "SQL va NoSQL ma'lumotlar bazalarining asosiy tushunchalari.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/8/87/Database-diagram.png", 
     "price": Decimal("27.99")},

    {"title": "Blokcheyn Texnologiyasi", "author": "Sardorbek Toshpulatov", "genre": "Blockchain", 
     "description": "Blokcheyn texnologiyasining ishlash tamoyillari.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Bitcoin_Blockchain_Transaction_Flow.svg", 
     "price": Decimal("49.99")},

    {"title": "Dasturiy Muhandislik", "author": "Malika Sobirova", "genre": "Software Engineering", 
     "description": "Dasturiy ta'minot yaratish jarayoni haqida batafsil.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Software_Engineering_Process.png", 
     "price": Decimal("32.99")},

    {"title": "Operatsion Tizimlar", "author": "Jamshidbek Shodibekov", "genre": "Operating Systems", 
     "description": "Operatsion tizimlarning ishlash prinsiplari haqida.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Operating_System_Concepts.png", 
     "price": Decimal("37.99")}
]

# Kitoblarni ma'lumotlar bazasiga yuklash
for book in books:
    Book.objects.create(
        title=book["title"],
        author=book["author"],
        genre=book["genre"],
        description=book["description"],
        image=book["image"],  # Google'dan URL orqali yuklanadi
        price=book["price"]
    )

print("Kitoblar muvaffaqiyatli qo'shildi!")
