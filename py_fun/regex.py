import re


def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

print '1.',get_matching_words(r'x')
print '2.',get_matching_words(r'ss')
print '3.',get_matching_words(r'e$')
print '4.',get_matching_words(r'b.b')
print '5.',get_matching_words(r'b.+b')
print '6.',get_matching_words(r'b.*b')
print '7.',get_matching_words(r'aeiou')
print '8.',get_matching_words(r'r*e*g*u*l*a*x*p*s*i*o*n*')
print '9.',get_matching_words(r'(.)\1')
