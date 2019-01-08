from Week6.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)

    print(ruby)
    print(python)
    print(visual_basic)

    language = []

    language.append(ruby)
    language.append(python)
    language.append(visual_basic)
    language.append(java)

    print("The dynamically typed languages are:")
    for i in language:
        if i.is_dynamic():
            print(i.name)

main()