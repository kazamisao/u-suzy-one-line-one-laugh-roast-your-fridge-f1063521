import os

TEXT = (
    "My phone keeps begging me to delete my own photos so System Data can "
    "stretch out — I paid for this phone, yet somehow I'm the tenant and "
    "System Data is the landlord."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
