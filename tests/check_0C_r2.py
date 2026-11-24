"""0C 第⼆輪的檢查：類別清單要有「外套」，⽽且可以登記。"""
import service
from config import CATEGORIES
from checklib import check, new_db
db = new_db()
check("0C-r2 類別清單有眼鏡", "外套" in CATEGORIES, True)
check("0C-r2 可以登記眼鏡", service.report_found(db, "外套", "操場")["ok"],
True)
check("0C-r2 「其他」仍然是最後⼀個類別", CATEGORIES[-1], "其他")