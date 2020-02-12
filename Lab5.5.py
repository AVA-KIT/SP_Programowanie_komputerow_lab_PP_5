password = input('Podaj hasło: ')

def doesItMeetRequrements(password):
    if len(password) >= 6:
        if len(password) <= 12:
            if password.isspace() == False:
                if password.isalnum() == False:
                    passset = set(list(password))
                    specset = set(['$','#','@'])
                    emptyset = set()
                    interset = passset.intersection(specset)
                    if interset != emptyset:
                        diffset = passset.difference(interset)
                        difflist = list(diffset)
                        diffstr = ''.join(difflist)
                        if diffstr.isdigit() == False:
                            if diffstr.isalpha() == False:
                                if password.islower() == False:
                                    if password.isupper() == False:
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

print(doesItMeetRequrements(password), end=" - ")
if doesItMeetRequrements(password) == True:
    print('wprowadzone hasło spełnia wymagania stawiane przez system logowania :-)')
else:
    print('wprowadzone hasło nie spełnia wymagania stawiane przez system logowania :-(')
