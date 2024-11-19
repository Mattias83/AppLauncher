import sys

from app_launcher import Application


def main() -> None:
    app = Application()
    app.run(sys.argv)


if __name__ == "__main__":
    main()
