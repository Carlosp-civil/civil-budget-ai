from pathlib import Path

#
# Root directories
#

APP_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = APP_DIR.parent

#
# Knowledge
#

KNOWLEDGE_DIR = APP_DIR / "knowledge"

DOMAIN_ALIASES_FILE = KNOWLEDGE_DIR / "domain_aliases.json"

#
# Export
#

EXPORT_DIR = PROJECT_ROOT / "exports"

#
# Temporary files
#

TEMP_DIR = PROJECT_ROOT / "tmp"