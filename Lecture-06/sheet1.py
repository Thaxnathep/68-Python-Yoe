def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    """
    ฟังก์ชันหาลำดับคำที่ต่อเนื่องและไม่ซ้ำกันยาวที่สุด
    รับ: words -> list ของ list ของคำ
    คืนค่า: tuple (ความยาวสูงสุด, list ของลำดับคำที่ยาวสุด)
    """
    # แปลงลิสต์ 2 มิติเป็นลิสต์ 1 มิติ
    flat_words = [w for sub in words for w in sub]
    # ตัวอย่าง: [["apple","banana"],["apple"]] → ["apple","banana","apple"]

    start = 0               # ตัวชี้จุดเริ่มต้นของลำดับคำไม่ซ้ำ
    seen = {}               # เก็บตำแหน่งล่าสุดของแต่ละคำ
    max_len = 0             # เก็บความยาวลำดับคำไม่ซ้ำที่ยาวที่สุด
    results = []            # เก็บลำดับคำที่ยาวที่สุดทั้งหมด

    # วนลูปผ่านแต่ละคำพร้อมตำแหน่ง
    for end, word in enumerate(flat_words):
        # ถ้าคำนี้เคยเจอและอยู่ในลำดับปัจจุบัน
        if word in seen and seen[word] >= start:
            start = seen[word] + 1   # เลื่อนจุดเริ่มต้นไปหลังคำซ้ำล่าสุด
        seen[word] = end              # อัปเดตตำแหน่งล่าสุดของคำ

        # คำนวณความยาวลำดับปัจจุบัน
        current_len = end - start + 1
        current_seq = flat_words[start:end + 1]  # ลำดับคำปัจจุบัน

        # ถ้ายาวที่สุดที่เจอใหม่
        if current_len > max_len:
            max_len = current_len
            results = [current_seq]   # เก็บลำดับคำนี้
        elif current_len == max_len:
            results.append(current_seq)  # ถ้ายาวเท่ากับ max_len → เก็บด้วย

    return (max_len, results)  # คืนค่าความยาวสูงสุดและลิสต์ลำดับคำที่ยาวที่สุด

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])