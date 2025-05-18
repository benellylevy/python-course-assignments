#כאן ניצור פונקציה שמקבלת רשימת מילים, ואז היא עוברת מילה מילה ואם המילה מופיע במילון שפתחנו היא מקבלת +1 לספירה, אם לאו אנחנו נוסיף את המילה כערך חדש במילון ונצמיד לו את הסיפרה 1.
def count_words(word_list):
    word_count = {}  # מילון לשמירת ספירת המילים
    for word in word_list:
        if word in word_count:
            word_count[word] += 1  # אם המילה כבר קיימת, נוסיף 1 לערך שלה
        else:
            word_count[word] = 1  # אם המילה לא קיימת, נוסיף אותה עם הערך 1
    return word_count

# דוגמה לשימוש
words = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']
result = count_words(words)
print(result)