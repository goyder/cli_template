"""
main.py 
"""

import os
import argparse
import yaml
import logging
import logging.config

def establish_logging(verbosity=0):
    """
    Establish logging for the app.
    """
    # Attempt to load the config file; otherwise give warning and default to standard
    LOGGING_CONFIG="logging.yaml"
    if verbosity >= 1:
        LOGGING_CONFIG="logging.verbose.yaml"
    if os.path.exists(LOGGING_CONFIG):
        with open(LOGGING_CONFIG, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    return logger


if __name__ == "__main__":

    # Parse arguments
    PROGRAM_DESCRIPTION = "DEFAULT DESCRIPTION"
    parser = argparse.ArgumentParser(PROGRAM_DESCRIPTION)
    parser.add_argument('-v', '--verbosity', action="count", help="Enable verbose output to file", default=0)
    args = parser.parse_args()

    # Establish logging
    logger = establish_logging(verbosity=args.verbosity)

    # Entry point goes here