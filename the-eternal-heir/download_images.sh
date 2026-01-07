#!/bin/bash
# Download images for Eternal Heir report

cd "$(dirname "$0")"
mkdir -p images

echo "📥 Downloading competitor book covers..."

# Direct competitors
curl -s -o "images/competitor_discovery_of_witches.jpg" "https://covers.openlibrary.org/b/isbn/9780670022412-L.jpg"
curl -s -o "images/competitor_interview_vampire.jpg" "https://covers.openlibrary.org/b/isbn/9780345476876-L.jpg"
curl -s -o "images/competitor_ninth_house.jpg" "https://covers.openlibrary.org/b/isbn/9781250313072-L.jpg"
curl -s -o "images/competitor_fledgling.jpg" "https://covers.openlibrary.org/b/isbn/9780446697612-L.jpg"
curl -s -o "images/competitor_cruel_prince.jpg" "https://covers.openlibrary.org/b/isbn/9780316310314-L.jpg"

# Indirect competitors
curl -s -o "images/competitor_indirect_dead_until_dark.jpg" "https://covers.openlibrary.org/b/isbn/9780441008536-L.jpg"
curl -s -o "images/competitor_indirect_twilight.jpg" "https://covers.openlibrary.org/b/isbn/9780316015844-L.jpg"
curl -s -o "images/competitor_indirect_passage.jpg" "https://covers.openlibrary.org/b/isbn/9780345504968-L.jpg"

echo "📥 Downloading persona book covers..."

# Maya Chen's books
curl -s -o "images/persona_book_interview_with_the_vampire.jpg" "https://covers.openlibrary.org/b/isbn/9780345476876-L.jpg"
curl -s -o "images/persona_book_ninth_house.jpg" "https://covers.openlibrary.org/b/isbn/9781250313072-L.jpg"
curl -s -o "images/persona_book_cruel_prince.jpg" "https://covers.openlibrary.org/b/isbn/9780316310314-L.jpg"

# Anika Patel's books
curl -s -o "images/persona_book_let_the_right_one_in.jpg" "https://covers.openlibrary.org/b/isbn/9780312603816-L.jpg" || curl -s -o "images/persona_book_let_the_right_one_in.jpg" "https://covers.openlibrary.org/b/isbn/9781847246678-L.jpg"
curl -s -o "images/persona_book_historian.jpg" "https://covers.openlibrary.org/b/isbn/9780316015844-L.jpg" || curl -s -o "images/persona_book_historian.jpg" "https://covers.openlibrary.org/b/isbn/9780316067928-L.jpg"
curl -s -o "images/persona_book_girl_with_dragon_tattoo.jpg" "https://covers.openlibrary.org/b/isbn/9780307269751-L.jpg"

echo ""
echo "👤 Generating persona avatars..."
curl -s -o "images/persona_maya_chen.png" "https://ui-avatars.com/api/?name=Maya+Chen&size=512&background=random&color=fff&bold=true"
curl -s -o "images/persona_anika_patel.png" "https://ui-avatars.com/api/?name=Anika+Patel&size=512&background=random&color=fff&bold=true"

echo ""
echo "✅ Image download complete!"
echo "📁 Images saved to: $(pwd)/images"

