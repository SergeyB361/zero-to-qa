def discount_code(is_vip: bool, has_coupon: bool) -> str:
    if is_vip and has_coupon:
        return "vip+coupon"
    if is_vip:
        return "vip"
    if has_coupon:
        return "coupon"
    return "none"


if __name__ == "__main__":
    print(discount_code(True, False))
