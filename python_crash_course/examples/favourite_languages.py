favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is "
    + language.title() + ".")

for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favourite language is " +
        favourite_languages[name].title() + "!")

for language in favourite_languages.values():
    print(language.title())