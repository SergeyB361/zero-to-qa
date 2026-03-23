ORDERS = {
    1: {"id": 1, "status": "new", "total": 100},
    2: {"id": 2, "status": "paid", "total": 250},
}


def get_order(order_id: int, token: str | None) -> tuple[int, dict[str, object]]:
    if token != "valid-token":
        return 401, {"error": "unauthorized"}
    if order_id not in ORDERS:
        return 404, {"error": "not found"}
    return 200, ORDERS[order_id]


def create_order(payload: dict[str, object]) -> tuple[int, dict[str, object]]:
    if payload.get("total") is None:
        return 400, {"error": "total is required"}
    if not isinstance(payload.get("total"), int):
        return 400, {"error": "total must be int"}
    return 201, {"id": 3, "status": "new", "total": payload["total"]}
