#list of current_users
current_users = ["david doee" , "shully doe" , "wendy doe" , "jane doe" , " eddy murphy"]
#list of new_users
new_users = [ "asare benny" , "john macaroid" , "godfred Owusu" , "berny canan" , "Edward sargeng"]
# Loop through current_ users and check for uniqueness
for username in current_users:
    if username in new_users:
        print(f"The username '{username}'is not available please choose a different one  ")
    else :
        print (f"The username '{username}' is available")


for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 :
        print("Fizz")  
    elif number % 5 == 0 :
        print("Buzz")
    else:
        print(number)
