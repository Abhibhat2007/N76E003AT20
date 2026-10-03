import os
import zipfile
import hashlib
import json
import argparse

parser = argparse.ArgumentParser(description="Package N76E003 Arduino Core & Update Index")
parser.add_argument("--user", default=None, help="GitHub username (e.g. your-name)")
parser.add_argument("--repo", default="arduino-n76e003", help="GitHub repo name (default: arduino-n76e003)")
args = parser.parse_args()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BASE_DIR, "hardware", "nuvoton", "8051")
ZIP_NAME = "n76e003-arduino-1.0.0.zip"
ZIP_PATH = os.path.join(BASE_DIR, ZIP_NAME)
INDEX_JSON_PATH = os.path.join(BASE_DIR, "package_nuvoton_n76e003_index.json")

print(f"Creating {ZIP_NAME} from core directory...")

with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(CORE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, CORE_DIR)
            archive_path = os.path.join("8051", rel_path)
            zf.write(full_path, archive_path)

file_size = os.path.getsize(ZIP_PATH)
sha256 = hashlib.sha256()
with open(ZIP_PATH, "rb") as f:
    while chunk := f.read(65536):
        sha256.update(chunk)
checksum = "SHA-256:" + sha256.hexdigest()

print(f"Archive created: {ZIP_PATH}")
print(f"Size: {file_size} bytes")
print(f"Checksum: {checksum}")

if os.path.exists(INDEX_JSON_PATH):
    with open(INDEX_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    pkg = data["packages"][0]
    platform = pkg["platforms"][0]
    platform["size"] = str(file_size)
    platform["checksum"] = checksum
    
    if args.user:
        pkg["websiteURL"] = f"https://github.com/{args.user}/{args.repo}"
        pkg["help"]["online"] = f"https://github.com/{args.user}/{args.repo}/issues"
        platform["help"]["online"] = f"https://github.com/{args.user}/{args.repo}"
        platform["url"] = f"https://github.com/{args.user}/{args.repo}/releases/download/v1.0.0/{ZIP_NAME}"
        print(f"Updated URLs for GitHub user: {args.user}, repo: {args.repo}")
        
    with open(INDEX_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Updated package_nuvoton_n76e003_index.json with exact size, checksum, and URLs!")
