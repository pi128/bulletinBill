def save_code(code: str, filename: str):
    with open(f"generated/{filename}", "w") as f:
        f.write(code)