from sqlmodel import Session
from database import engine, create_db
from models import Warehouse, Item, ClaimEvent, EventLog
from datetime import datetime


def seed():
    create_db()

    with Session(engine) as session:

        # 倉庫
        warehouses = [
            Warehouse(wh_id="WH001", wh_name="桃園一倉", region="北區"),
            Warehouse(wh_id="WH002", wh_name="台中倉", region="中區"),
            Warehouse(wh_id="WH003", wh_name="高雄倉", region="南區"),
            Warehouse(wh_id="WH004", wh_name="桃園二倉", region="北區"),
        ]
        for w in warehouses:
            session.add(w)

        # 商品
        items = [
            Item(item_id="ITM-A001", item_name="無線耳機 Pro", category="3C"),
            Item(item_id="ITM-A002", item_name="充電線 USB-C", category="配件"),
            Item(item_id="ITM-B001", item_name="保溫瓶 500ml", category="生活"),
            Item(item_id="ITM-C001", item_name="藍牙喇叭", category="3C"),
        ]
        for i in items:
            session.add(i)

        # Claim 事件
        events = [
            ClaimEvent(
                event_id="EVT-20250501-001",
                from_wh="WH001", to_wh="WH002",
                item_id="ITM-A001", prb_code="1-2",
                qty_claimed=5, status="待確認",
                note="轉倉收到5件，短少5件",
                created_at=datetime(2025, 5, 1, 9, 0)
            ),
            ClaimEvent(
                event_id="EVT-20250502-002",
                from_wh="WH003", to_wh="WH001",
                item_id="ITM-B001", prb_code="1-2",
                qty_claimed=3, status="確認",
                note="確認短少，已補帳",
                created_at=datetime(2025, 5, 2, 10, 0)
            ),
            ClaimEvent(
                event_id="EVT-20250503-003",
                from_wh="WH002", to_wh="WH004",
                item_id="ITM-A002", prb_code="1-7",
                qty_claimed=10, status="異議",
                note="我方紀錄發出10件",
                created_at=datetime(2025, 5, 3, 11, 0)
            ),
            ClaimEvent(
                event_id="EVT-20250504-004",
                from_wh="WH001", to_wh="WH003",
                item_id="ITM-C001", prb_code="1-2",
                qty_claimed=2, status="待確認",
                note="GCGP箱數正確但內容物少",
                created_at=datetime(2025, 5, 4, 8, 30)
            ),
        ]
        for e in events:
            session.add(e)

        # Event log
        logs = [
            EventLog(event_id="EVT-20250501-001", action="建立", actor_wh="WH001", note="轉倉收到5件短少", timestamp=datetime(2025, 5, 1, 9, 0)),
            EventLog(event_id="EVT-20250501-001", action="查看", actor_wh="WH002", note="台中倉已查看", timestamp=datetime(2025, 5, 1, 11, 32)),
            EventLog(event_id="EVT-20250502-002", action="建立", actor_wh="WH003", note="進貨短少3件", timestamp=datetime(2025, 5, 2, 10, 0)),
            EventLog(event_id="EVT-20250502-002", action="確認", actor_wh="WH001", note="確認短少，已補帳", timestamp=datetime(2025, 5, 2, 14, 30)),
            EventLog(event_id="EVT-20250503-003", action="建立", actor_wh="WH002", note="效期短少10件", timestamp=datetime(2025, 5, 3, 11, 0)),
            EventLog(event_id="EVT-20250503-003", action="異議", actor_wh="WH004", note="我方紀錄發出10件，請提供證明", timestamp=datetime(2025, 5, 3, 14, 0)),
            EventLog(event_id="EVT-20250504-004", action="建立", actor_wh="WH001", note="GCGP箱數正確但內容物少", timestamp=datetime(2025, 5, 4, 8, 30)),
        ]
        for l in logs:
            session.add(l)

        session.commit()
        print("✅ 假資料建立完成！")


if __name__ == "__main__":
    seed()