import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open("./config.json") as f:
    config = json.load(f)

RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
THUMBNAIL_DIR = os.path.join(RESOURCES_DIR, "thumbnail")
TOP8_DIR = os.path.join(RESOURCES_DIR, "top-8")
FONTS_DIR = os.path.join(RESOURCES_DIR, "fonts")
ASSET_DIR = os.path.join(RESOURCES_DIR, "assets")

APP_DIR = os.path.join(ROOT_DIR, "app")
UI_DIR = os.path.join(ROOT_DIR, "ui")

OUTPUT_DIR = config["output_dir"]
RENDERS_DIR = config["render_dir"]
