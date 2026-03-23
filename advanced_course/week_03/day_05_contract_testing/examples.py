EXPECTED_CONTRACT = {
    "required_fields": {"id", "status", "total"},
    "status_values": {"new", "paid", "cancelled"},
}


def contract_matches(payload: dict[str, object]) -> bool:
    fields_ok = EXPECTED_CONTRACT["required_fields"].issubset(payload)
    status_ok = payload.get("status") in EXPECTED_CONTRACT["status_values"]
    return fields_ok and status_ok


if __name__ == "__main__":
    print(contract_matches({"id": 1, "status": "paid", "total": 100}))
