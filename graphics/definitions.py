import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
THUMBNAIL_DIR = os.path.join(RESOURCES_DIR, 'thumbnail')
# Hard coded for now
# These are the renders from the other repo
# Consider making them a submodule?
RENDERS_DIR = "D:\\TrainingGrounds-Graphics\\Character Renders"

APP_DIR = os.path.join(ROOT_DIR, 'app')
UI_DIR = os.path.join(ROOT_DIR, 'ui')

OUTPUT_DIR = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\Output')
