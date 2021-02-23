
items = input("écrivez une séquence de mot séparés par des virgules")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))