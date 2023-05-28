import re

def count_login_attempts(ip_address):

  with open("ssh_logs_sample", "r") as f:
    lines = f.readlines()

  count = 0
  for line in lines:
    match = re.search(r"Failed password for .* from {}".format(ip_address), line)
    if match:
      count += 1

  return count

if __name__ == "__main__":
  ip_address = input("Enter the IP address: ")

  count = count_login_attempts(ip_address)

  print("The number of login attempts from {} is {}.".format(ip_address, count))