import re


class Preprocess():
    def __init__(self) -> None:
        pass


    def remove_usernames(self, text):
        clean_text = re.sub(r'@\w+', '', text)
        return clean_text


    def remove_numbers(self, text):
        clean_text = re.sub(r'\d+', '', text)
        return clean_text


    def remove_links(self, text):
        URL_REGEXES = [
            r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
            r"@(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$@iS",
            r"http[s]?://[a-zA-Z0-9_\-./~\?=%&]+",
            r"www[a-zA-Z0-9_\-?=%&/.~]+",
            r"[a-zA-Z]+\.com",
            r"(?=http)[^\s]+",
            r"(?=www)[^\s]+",
            r"://",
        ]

        for reg in URL_REGEXES:
            text = re.sub(reg, '', text)
        return text


    def remove_diacritics(self, text):
        arabic_diacritics = re.compile("""
                                ّ    | # Tashdid
                                َ    | # Fatha
                                ً    | # Tanwin Fath
                                ُ    | # Damma
                                ٌ    | # Tanwin Damm
                                ِ    | # Kasra
                                ٍ    | # Tanwin Kasr
                                ْ    | # Sukun
                                ـ    | # Tatwil/Kashida
                            """, re.VERBOSE)
        return re.sub(arabic_diacritics, '', text)


    def normalize_chars(self, text):
        preprocessed_text = re.sub("[إأآا]", "ا", text)
        preprocessed_text = re.sub("ى", "ي", preprocessed_text)
        preprocessed_text = re.sub("ؤ", "ء", preprocessed_text)
        preprocessed_text = re.sub("ئ", "ء", preprocessed_text)
        preprocessed_text = re.sub("ة", "ه", preprocessed_text)
        preprocessed_text = re.sub("گ", "ك", preprocessed_text)
        preprocessed_text = re.sub("ڤ", "ف", preprocessed_text)
        preprocessed_text = re.sub("چ", "ج", preprocessed_text)
        preprocessed_text = re.sub("ژ", "ز", preprocessed_text)
        preprocessed_text = re.sub("پ", "ب", preprocessed_text)
        preprocessed_text = re.sub("&quot;", " ", preprocessed_text)
        # preprocessed_text = re.sub("?", " ? ", preprocessed_text)
        preprocessed_text = re.sub("؟", " ? ", preprocessed_text)
        preprocessed_text = re.sub("¿", " ¿ ", preprocessed_text)
        preprocessed_text = re.sub("!", " ! ", preprocessed_text)
        preprocessed_text = re.sub("@", " ", preprocessed_text)
        preprocessed_text = re.sub("#", " ", preprocessed_text)
        preprocessed_text = re.sub("،", " ", preprocessed_text)
        preprocessed_text = re.sub("ـ", " ", preprocessed_text)
        preprocessed_text = re.sub("؛", " ", preprocessed_text)
        preprocessed_text = re.sub(":", " ", preprocessed_text)
        preprocessed_text = re.sub("'", " ", preprocessed_text)
        preprocessed_text = re.sub("‘", " ", preprocessed_text)
        preprocessed_text = re.sub("’", " ", preprocessed_text)
        preprocessed_text = re.sub("“", " ", preprocessed_text)
        preprocessed_text = re.sub("”", " ", preprocessed_text)
        preprocessed_text = re.sub("-", " ", preprocessed_text)
        preprocessed_text = re.sub("=", " ", preprocessed_text)
        preprocessed_text = re.sub("_", " ", preprocessed_text)
        preprocessed_text = re.sub("\)", " ", preprocessed_text)
        preprocessed_text = re.sub("\(", " ", preprocessed_text)
        preprocessed_text = re.sub("\[", " ", preprocessed_text)
        preprocessed_text = re.sub("\]", " ", preprocessed_text)
        preprocessed_text = re.sub("{", " ", preprocessed_text)
        preprocessed_text = re.sub("}", " ", preprocessed_text)
        preprocessed_text = re.sub("~", " ", preprocessed_text)
        preprocessed_text = re.sub("`", " ", preprocessed_text)
        preprocessed_text = re.sub("«", " ", preprocessed_text)
        preprocessed_text = re.sub("»", " ", preprocessed_text)

        return preprocessed_text


    def remove_repeated_chars(self, text):
        pattern = re.compile(r"(.)\1{2,}")
        clean_text = pattern.sub(r"\1\1", text)
        return clean_text


    def remove_extra_whitespaces(self, text):
        clean_text = re.sub(r'\s+', ' ', text)
        return clean_text.strip()


    def preprocessing(self, text):

        #lower case
        text = text.lower()

        #user_names
        text = self.remove_usernames(text)

        #numbers
        text = self.remove_numbers(text)

        #links
        text = self.remove_links(text)

        #tashkel
        text = self.remove_diacritics(text)

        #normalizeChars
        text = self.normalize_chars(text)

        #repeated charachters
        text = self.remove_repeated_chars(text)

        #white_space
        text = self.remove_extra_whitespaces(text)

        return text