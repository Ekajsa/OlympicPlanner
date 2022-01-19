import os


def main():
    print(os.urandom(32).hex())


if __name__ == '__main__':
    main()
