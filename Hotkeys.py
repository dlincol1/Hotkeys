# Store Hotkeys in dictionary for use in Hotkeys.html
# Copy code to VRED VariantSet Script tab and name as 'Hotkeys'
# By Dan Lincoln

print "Getting Hotkeys..."
print "Supported Keys for this version (0-9, A-Z):"
vsetPtrs = getVariantSets()

# Build a list of names for iteration, cannot just iterate on the Ptr names
vsets = []
hkeys = []
keys_active = []
key_numbers = []
keys_supported = [
'1','2','3','4','5','6','7','8','9','0',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Dictionary of keys & values
hotkeyDictionary = {}

for i in vsetPtrs:
    vsets.append(i)

for j in vsets:
    v = getVariantSet(j)
    h = v.getHotkey()

    if h != "":
        # remove spaces
        dictKey = h.strip()
        hkeys.append(h.strip())
        if len(h.strip()) == 1:
            keys_active.append(h.strip()) 
        hotkeyDictionary[dictKey] = j

hkeys.sort()
keys_active.sort()

print "Hotkeys found: " + str(hkeys)
print "Dictionary keys: " + str(hotkeyDictionary.keys())
print "Dictionary values: " + str(hotkeyDictionary.values())