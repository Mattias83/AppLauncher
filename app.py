import sys

from app_launcher.application import Application


def main() -> None:
    app = Application()
    app.run(sys.argv)


if __name__ == "__main__":
    main()
