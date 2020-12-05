# Store Hotkeys in dictionary for use in Hotkeys.html App
# Copy to VRED VSet Script tab and name as 'Hotkeys'
# By Dan Lincoln

filename = getFileIOFilePath()
print("\n" + filename)
print("Hotkey : Variant Set Name")
print("-------------------------")
vset_names = getVariantSets()

hotkeys_all = []
hotkeys_single = []
hotkeyDict = {}

# Append keys to lists
for j in vset_names:
    v = getVariantSet(j)
    hotkey = v.getHotkey()
    
    if hotkey != "":
        hotkeys_all.append(hotkey)

        single_key = hotkey.strip()
        if len(single_key) == 1:
            hotkeys_single.append(single_key)
        hotkeyDict[hotkey] = j

hotkeys_all.sort()
hotkeys_single.sort()

for i in hotkeys_all:
    print((i + " : " + str(hotkeyDict[i]) ))