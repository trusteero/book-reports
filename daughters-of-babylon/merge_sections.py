#!/usr/bin/env python3
"""
Merge the 5 section JSON files into a single consolidated JSON file
"""

import json
import sys
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Define input files
section1_file = script_dir / "DaughtersofBabylon_SECTION1_OVERVIEW.txt"
section2_file = script_dir / "DaughtersofBabylon_SECTION2_Demographics5.2UTF8.txt"
section3_file = script_dir / "DaughtersofBabylon_SECTION3_Classification5.2UTF8.txt"
section4_file = script_dir / "DaughtersofBabylon_SECTION4_Personas5.2UTF8.txt"
section5_file = script_dir / "DaughtersofBabylon_SECTION5_Marketingv5.2UTF8.txt"

# Output file
output_file = script_dir / "daughters-of-babylon.json"

def load_json_file(filepath):
    """Load a JSON file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        sys.exit(1)

def main():
    print("📚 Merging sections for Daughters of Babylon...")
    
    # Load Section 1 (already a JSON object)
    print(f"  Loading Section 1: {section1_file.name}")
    section1 = load_json_file(section1_file)
    
    # Load Section 2 (JSON array with demographics)
    print(f"  Loading Section 2: {section2_file.name}")
    section2_data = load_json_file(section2_file)
    demographics = section2_data[0].get("demographics", {}) if isinstance(section2_data, list) else section2_data.get("demographics", {})
    
    # Load Section 3 (JSON array with classification)
    print(f"  Loading Section 3: {section3_file.name}")
    section3_data = load_json_file(section3_file)
    classification = section3_data[0].get("classification", {}) if isinstance(section3_data, list) else section3_data.get("classification", {})
    
    # Load Section 4 (JSON array with readerPersonas)
    print(f"  Loading Section 4: {section4_file.name}")
    section4_data = load_json_file(section4_file)
    readerPersonas = section4_data[0].get("readerPersonas", {}) if isinstance(section4_data, list) else section4_data.get("readerPersonas", {})
    
    # Load Section 5 (JSON array with marketing)
    print(f"  Loading Section 5: {section5_file.name}")
    section5_data = load_json_file(section5_file)
    marketing = section5_data[0].get("marketing", {}) if isinstance(section5_data, list) else section5_data.get("marketing", {})
    
    # Merge everything into a single JSON object
    merged = {
        **section1,  # This includes: book, audienceMatch, analysisOverview, moodAndTone
        "demographics": demographics,
        "classification": classification,
        "readerPersonas": readerPersonas,
        "marketing": marketing
    }
    
    # Write the merged JSON to output file
    print(f"  Writing merged JSON to: {output_file.name}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully merged all sections into {output_file}")
    print(f"   Output file: {output_file.absolute()}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

