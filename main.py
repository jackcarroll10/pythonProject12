def palindrome_checker(list):
    list2 = list[:]
    list.reverse()
    if list2 == list:
        print('Palindrome')
    else:
        print('Not Palindrome')


user_list = []
user_input = (input('Enter list of words'))
user_list = user_input.split()
palindrome_checker(user_list)