
MAX_TRIES = 5   # (file-)global variable

if MAX_TRIES > 1:
    color = "purple"

def doit(word):
    x = len(word)
    for t in range(MAX_TRIES):
        print(f"trying {word}...")
    print(f"{x = }")
    
doit("wombat")
doit("skunk")
