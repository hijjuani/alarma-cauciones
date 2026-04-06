from scraper import create_driver, get_tasas
from ui import create_ui, update_ui
from config import TARGET_ARS, TARGET_USD, REFRESH_SECONDS

def main():
    driver = create_driver()
    widgets = create_ui()

    prev = {
        "ars_1": None,
        "usd_1": None,
        "ars_7": None,
        "usd_7": None,
    }

    targets = {
        "ars": TARGET_ARS,
        "usd": TARGET_USD
    }

    def loop():
        try:
            data = get_tasas(driver)
            if data:
                update_ui(widgets, data, prev, targets)
        except Exception as e:
            print("Error:", e)

        widgets["root"].after(REFRESH_SECONDS * 1000, loop)

    loop()
    widgets["root"].mainloop()

if __name__ == "__main__":
    main()