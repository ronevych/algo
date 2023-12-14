def boyer_moore_search(haystack, needle):
    haystack_length = len(haystack)
    needle_length = len(needle)
    if needle_length == 0:
        return [i for i in range(haystack_length + 1)]
    last_occurrence = {}
    for i in range(needle_length - 1):
        last_occurrence[needle[i]] = needle_length - 1 - i
    result = []
    i = needle_length - 1
    while i < haystack_length:
        j = needle_length - 1
        k = i
        while j >= 0 and haystack[k] == needle[j]:
            j -= 1
            k -= 1
        if j == -1:
            result.append(k + 1)
        i += last_occurrence.get(haystack[i], needle_length)
    return result


haystack = "kvadratatkvadrat"
needle = "kvadrat"
result = boyer_moore_search(haystack, needle)
print(f"Індекси входжень '{needle}' в '{haystack}': {result}")


