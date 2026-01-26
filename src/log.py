import logging


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        # %(levelname).1s takes the first character of the level name (I, W, E, etc.)
        # %(msecs)03d prints millisecs, something that datefmt does not offer
        format="%(levelname).1s %(asctime)s.%(msecs)03d [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
