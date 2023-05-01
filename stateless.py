""" Stateless functions. """
""" do not change the side effects """
""" referential trasparency - allows parallel execution and functions can be tested seperately """

# stateful function rely
# only on the variables of the functions
def speak(speaker: str, text: str) -> str:
    return "[%s] %s" % (speaker, text)

print(speak("John", "hello world"))


def smile(l: list[int]) -> list[str]:
    return ["."] * sum(l)

assert(smile([1,3]) ==  [".", ".", ".", "."])
