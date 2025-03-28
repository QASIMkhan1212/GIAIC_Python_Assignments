print("Mad Libs - 3-Line Story!")
adj = input("Adjective: ")
noun = input("Noun: ")
verb_past = input("Verb (past tense): ")
adverb = input("Adverb: ")
emotion = input("Emotion: ")
place = input("Place: ")

story = (
    f"A {adj} {noun} once {verb_past} {adverb} under the moonlight,\n"
    f"Suddenly feeling {emotion}, it vanished without a trace,\n"
    f"Only to reappear in {place}, covered in glitter!"
)

print("\nYour Story:\n" + story)