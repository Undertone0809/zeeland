from zeeland import Logger


def main():
    logger = Logger("test")
    logger_framework = Logger("test_framework")

    logger.info("Hello, world!")
    logger_framework.info("Hello, world!")

    # Both framework's log files will record this exception
    raise ValueError("test")


if __name__ == "__main__":
    main()
