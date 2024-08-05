user = "Johnny"
privileged_users = ["Tom", "Albert", "Stephen"]
if user in privileged_users:
    print(f"Welcome home {user}")
else:
    print("INTRUDER ALLERT. Silently calling police...")


my_dict = {"name": "Steven", "born": "1955-02-24", "interests": "Apples"}
if my_dict["name"] == "Steven":
    print("This guy does not like Windows")
else:
    print("No clue who this is")