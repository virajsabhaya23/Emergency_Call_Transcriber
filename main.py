# Import testCases dictionary
from testCases import test_cases

# Implement the String Edit Distance Algorithm function
def stringEditDistance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table with base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]

# matching the names functionally
def matchNames(inputNames, dmvRecords):
    matched_addresses = []
    for name in inputNames:
        min_edit_distance = float("inf")
        closest_match = ""

        for record in dmvRecords:
            record_name, address = record.split(";")
            distance = stringEditDistance(name, record_name)

            if distance < min_edit_distance:
                min_edit_distance = distance
                closest_match = address

        matched_addresses.append(closest_match)

    return matched_addresses

def main():
    # passing single test case
    testCaseName = "test_3"

    # begin testing
    inputNames, dmvRecords, expectedOutput = test_cases[testCaseName]
    user_output = matchNames(inputNames, dmvRecords)

    print(f"INPUT:\n{inputNames},\n{dmvRecords}\n")
    print(f"EXPECTED OUTPUT: {expectedOutput}\n")
    print(f"YOUR OUTPUT: {user_output}\n")

    if user_output == expectedOutput:
        print(f"---\n{testCaseName} passed successfully :)\n---")
    else:
        print(f"{testCaseName} failed :(")

if __name__ == "__main__":
    main()