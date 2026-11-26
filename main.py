import os

TEXT = (
    "I am sorry I watered your plastic fern for 41 days while the real basil "
    "beside it filed for neglect.\n"
    "I learned a leaf that never changes is data, not devotion; I will check "
    "the soil before I trust the green.\n"
)


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
