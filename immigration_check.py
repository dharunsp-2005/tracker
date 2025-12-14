def immigration_clearance(passport_valid, visa_status, watchlist):
    if not passport_valid:
        return "Denied: Invalid Passport"
    if visa_status != "Valid":
        return "Denied: Invalid Visa"
    if watchlist:
        return "Flagged: Security Review"
    return "Cleared"
