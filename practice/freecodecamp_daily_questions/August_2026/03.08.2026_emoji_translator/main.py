# Emoji Translator (freeCodeCamp)
#
# Given a string of emojis, return the phrase using the following table:
#
# Emoji    Word
# 👶       "baby"
# 🐱       "cat"
# 🐕       "dog"
# 🐟       "fish"
# 🥵       "hot"
# 🧊       "ice"
# 🪨       "rock"
# 🦈       "shark"
# 🍲       "soup"
# ⭐       "star"
#
# Return the words separated by spaces.
#
# Example:
# emojis = "👶🥵🍲"   -> "baby hot soup"


EMOJI_TO_WORD = {
    "👶": "baby",
    "🐱": "cat",
    "🐕": "dog",
    "🐟": "fish",
    "🥵": "hot",
    "🧊": "ice",
    "🪨": "rock",
    "🦈": "shark",
    "🍲": "soup",
    "⭐": "star",
}


def translate_emojis(emojis: str) -> str:
    k = list()
    for x in emojis:
        k.append(EMOJI_TO_WORD[x])

    return " ".join(k)
        


# Test cases
print(translate_emojis("👶🥵🍲"))     # baby hot soup
print(translate_emojis("🦈🐟🐕🐱"))   # shark fish dog cat
print(translate_emojis("⭐🧊🪨"))     # star ice rock
