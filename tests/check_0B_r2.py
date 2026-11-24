"""0B 第二輪的檢查：類別清單要有「錢包」，而且可以登記。"""
import service
from config import CATEGORIES
from checklib import check, new_db
db = new_db()
check("0B-r2 類別清單有錢包", "錢包" in CATEGORIES, True)
check("0B-r2 可以登記錢包", service.report_found(db, "錢包", "操場")["ok"],
True)
check("0B-r2 「其他」仍然是最後一個類別", CATEGORIES[-1], "其他")