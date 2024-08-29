import requests

def fetch_random_user_freeApi():
  url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
  response = requests.get(url)
  data = response.json()

  if data["success"] and "data" in data:
    user_data = data["data"]
    user_name = user_data["login"] ["username"]
    user_country = user_data["location"] ["country"]
    return user_name, user_country
  else:
    raise Exception("Failed to fetch user data")

# protect to main() from crash using try catch
def main():
  try:
    user_name, user_country = fetch_random_user_freeApi()
    print(f"Username: {user_name} \n Country: {user_country}" )
  except Exception as exception:
    print(str(exception))

if __name__ == "__main__":
  main()