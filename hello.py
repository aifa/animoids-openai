import argparse
from openai import OpenAI
import yaml
from dotenv import load_dotenv
import os
import requests
import json
import sys




def submit():
    output_folder = os.getenv("OUTPUT_DIR")
    if output_folder:
        output_file = os.path.join(output_folder, "response.txt")
        with open(output_file, "w") as file:
            file.write("Hello, world!")
            print(f"Response saved to {output_file}")
    else:
        print("OUTPUT environment variable not defined. Response will not be saved.", file=sys.stderr)
    return 1





if __name__ == "__main__":
    #ipfs_url = "https://bafybeib76s7igm5ncpg3n3eno64bjhak62ua2gyqzdruaxvejngh4inxui.ipfs.w3s.link/Pope-Francis-Coat.jpg"
    # Parse command-line arguments
    submit()
    