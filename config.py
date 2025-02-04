from enum import Enum

###############################################################################
#
# Google Vision API Structures
#
###############################################################################

SYMBOL_STRUCTURE = {
  'name': 'symbols',
  'fields': ['confidence', 'text'],
  'objects': ['bounding_box', 'property']
}

WORD_STRUCTURE = {
  'name': 'words',
  'fields': ['confidence'],
  'objects': ['bounding_box', 'property'],
  'list': SYMBOL_STRUCTURE
}

PARAGRAPH_STRUCTURE = {
  'name': 'paragraphs',
  'fields': ['confidence'],
  'objects': ['bounding_box', 'property'],
  'list': WORD_STRUCTURE
}

BLOCK_STRUCTURE = {
  'name': 'blocks',
  'fields': ['block_type', 'confidence'],
  'objects': ['bounding_box', 'property'],
  'list': PARAGRAPH_STRUCTURE
}

PAGE_STRUCTURE = {
  'name': 'pages',
  'fields': ['confidence', 'height', 'width'],
  'objects': ['property'],
  'list': BLOCK_STRUCTURE
}

STRUCTURE = {
  'name': 'overall',
  'fields': ['text'],
  'objects': [],
  'list': PAGE_STRUCTURE
}

class StructureType(Enum):
  PAGE = 1
  BLOCK = 2
  PARA = 3
  WORD = 4
  SYMBOL = 5

###############################################################################
#
# Configurations
#
###############################################################################

# Directory to write json and image files to
WRITE_DIRECTORY = 'scans'

# Allowed formats for processing
ALLOWED_FORMATS = ['.pdf', '.png', '.jpg', '.jpeg']

# Path to credentials json for Google Vision API
CREDENTIALS_PATH = 'credentials/client_secret.json'

# Minimum number of characters to use to determine text orientation
#  - Higher = better chance of correct orientation detection
#  - Lower = better chance of finding a string longer than this length
ORIENTATION_DETECTION_THRESHOLD = 10

# Buffer space between columns
#  - Higher = more tolerant column width detection
#  - Lower = stricter column width detection
COLUMN_DETECTION_THRESHOLD = 15

# Resolution to save PDF images in
#  - Higher = better text recognition
#  - Lower = better memory usage
PAGE_RESOLUTION = 1200

# Image contrast enhancement level
#  - Higher = text may be clearer
#  - Lower = less chance of text blurring with background
IMAGE_CONTRAST = 2

# % matching characters to be included in the search results
SEARCH_THRESHOLD = 90
