
total_cookies = int(input())

number_of_friends = int(input())


if number_of_friends > 0:
    cookies_per_friend = total_cookies // number_of_friends
else:
    cookies_per_friend = 0


print(cookies_per_friend)
