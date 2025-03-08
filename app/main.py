from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_db_connection

app = FastAPI()

# CORS Ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/kitaplar")
async def kitaplari_getir():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT K.AD, Y.AD AS YAZAR 
        FROM KUTUPHANE_SHEMA.KITAP K 
        JOIN KUTUPHANE_SHEMA.YAZAR Y ON K.YAZAR_ID = Y.YAZAR_ID
    """)
    
    results = []
    for row in cursor:
        results.append({
            "kitap_adi": row[0],
            "yazar": row[1],
            "stok": row[2]
        })
    
    cursor.close()
    conn.close()
    
    return {"kitaplar": results}

@app.get("/kutuphaneler")
async def kutuphaneleri_getir():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT AD, SEHIR, ULKE FROM KUTUPHANE_SHEMA.KUTUPHANE")
    
    results = []
    for row in cursor:
        results.append({
            "ad": row[0],
            "sehir": row[1],
            "ulke": row[2]
        })
    
    cursor.close()
    conn.close()
    
    return {"kutuphaneler": results}