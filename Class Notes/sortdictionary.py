# if descending is True, the dictionary will be sorted from greatest to least value
# if descending is False, the dictionary will be sorted from least to greatest value
def sortDictionaryByValues(dictionaryName, descending):
    if (type(descending) != bool and type(dictionaryName) != dict):
        raise ValueError("sortDictionaryByValues requires a dictionary and boolean as arguments, respectively")
        return None
    else:
        sortedDictionary = {}
        sortedList = sorted(dictionaryName.items(),key=lambda x: x[1], reverse=descending)
        for item in sortedList:
            sortedDictionary[item[0]] = item[1]
        return sortedDictionary