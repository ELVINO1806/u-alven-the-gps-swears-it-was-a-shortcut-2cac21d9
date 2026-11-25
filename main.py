import os

ENTRY = "Shortcut confirmed: we saved four minutes and gained a toll booth, a goat, and a very long one-way street. The map takes no questions. I take even fewer."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
