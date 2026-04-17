def send_to_careergenie(candidate):
    print("\n=== INVITED CANDIDATE ===")
    print("Username:", candidate["username"])
    print("Score:", candidate["score"])
    print("Message:", candidate.get("message", "No message"))
    print("========================\n")