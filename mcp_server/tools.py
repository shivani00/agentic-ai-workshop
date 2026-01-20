def check_policy_status(claimant_name):
    return "ACTIVE"

def get_claim_history(claimant_name):
    if claimant_name.lower() == "john doe":
        return 1
    if claimant_name.lower() == "mark fraud":
        return 5
    return 0

def fraud_score(history):
    if history >= 4:
        return 0.9
    if history >= 2:
        return 0.6
    return 0.2
