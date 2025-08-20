survery = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

choices_sets = [set(p) for p in survery]
common_languages = set.intersection(*choices_sets)
print("1. Languages chosen by all praticipants:", common_languages)

common_languages = set.intersection(*choices_sets)
all_languages = set.union(*choices_sets)
only_choices = all_languages - common_languages
print("Languages chosen by some but not all:", only_choices)

print("2. Fine languages only choices: ", only_choices)

all_choise = set.union(*choices_sets)
all_choise_count = len(all_choise)
print("3. numbers of unique languages: ", all_choise_count)