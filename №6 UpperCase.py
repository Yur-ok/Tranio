import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'

UllUUU_1 = re.compile(r'[A-Z]{1}[a-z]{2}[A-Z]{3}')
UllUUU_2 = re.compile(r'([A-Z]{1})[a-z]{2}[A-Z]{2}([A-Z]{1})')

print('Use RegEx')
print(UllUUU_1.findall(line))
print(UllUUU_2.findall(line))
print('Total num of matching is: ', len(UllUUU_2.findall(line)) * 2, '\n')


def Uper_llUU_Uper(string):
    i = 0
    n = 0
    tmp = ''
    arr = []
    while i < len(string):
        if string[i].isupper():
            tmp = string[i]
            n = i + 1
            if n < len(string) and string[n].islower():
                n = i + 2
                if n < len(string) and string[n].islower():
                    n = i + 3
                    if n < len(string) and string[n].isupper():
                        n = i + 4
                        if n < len(string) and string[n].isupper():
                            n = i + 5
                            if n < len(string) and string[n].isupper():
                                arr.append(tmp)
                                arr.append(string[n])
                                i += 1
                            else:
                                if i < len(string):
                                    i += 1
                                continue
                        else:
                            if i < len(string):
                                i += 1
                            continue
                    else:
                        if i < len(string):
                            i += 1
                        continue
                else:
                    if i < len(string):
                        i += 1
                    continue
            else:
                if i < len(string):
                    i += 1
            continue
        else:
            if i < len(string):
                i += 1
            continue
    return arr


print('Use my own function.')
print(Uper_llUU_Uper(line))
print('Total num of matching is: ', len(Uper_llUU_Uper(line)))
