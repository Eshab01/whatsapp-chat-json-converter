import json
import argparse
from datetime import datetime

# Set up command-line arguments with defaults
parser = argparse.ArgumentParser(description="Convert chat logs to JSON format.")
parser.add_argument("input_file", nargs="?", default="chat.txt", help="
