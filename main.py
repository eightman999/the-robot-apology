import os

TEXT = (
    "I apologise: I read your baby's 3 a.m. cry as a calendar reminder and politely "
    "announced 'feeding time' to the whole house.\n"
    "I learned volume is not a notification setting; next time I will soothe first "
    "and schedule nothing."
)


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
