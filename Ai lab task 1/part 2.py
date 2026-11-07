def check_eligibility(score, documents_complete, attendance, interview_passed):

    if score < 70:
        return "Rejected: Score is below 70"

    if not documents_complete:
        return "Rejected: Documents are incomplete"

    if attendance < 75:
        return "Rejected: Attendance is below 75%"

    if not interview_passed:
        return "Rejected: Interview not passed"

    return "Eligible"


test_cases = [
    ("Test 1 - Pass", 80, True, 85, True),
    ("Test 2 - Attendance Failure", 80, True, 70, True),
    ("Test 3 - Interview Failure", 80, True, 85, False),
    ("Test 4 - Score Boundary", 70, True, 85, True)
]

for name, score, documents, attendance, interview in test_cases:
    result = check_eligibility(score, documents, attendance, interview)

    print("\n", name)
    print("Input:", score, documents, attendance, interview)
    print("Expected Result:", result)
    print("Actual Result:", result)
    print("Reason:", result)