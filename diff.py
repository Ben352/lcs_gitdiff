import argparse
class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  RESET = "\033[0m"

def main():
    parser = argparse.ArgumentParser(
        prog="",
        description="",
        epilog=""
    )
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument("-l","--level")
    args = parser.parse_args()

    with open(args.file1,"r") as f:
        contentA = f.read()
    with open(args.file2,"r") as f:
        contentB = f.read()

    if args.level == "word":
        wordsa = [x for x in contentA.split(" ")]
        wordsb = [x for x in contentB.split(" ")]
        contentA = wordsa
        contentB = wordsb
    if args.level == "line":
        wordsa = [x for x in contentA.split("\n")]
        wordsb = [x for x in contentB.split("\n")]
        contentA = wordsa
        contentB = wordsb
    return [contentA,contentB]
def LCS(s0,s1):
    dp = [
        [0 for _ in range(0,len(s1)+1)]
        for _ in range(0,len(s0)+1)
    ]
    for i in range(0,len(s0)+1):
        for x in range(0,len(s1)+1):
            if x == 0 or i == 0:
                continue
            else:
                if s0[i-1] == s1[x-1]:
                    dp[i][x] = 1 + dp[i-1][x-1]
                else:
                    dp[i][x] = max(dp[i][x-1],dp[i-1][x]) 
    return dp
def backtrack(dp,s0,s1,hashed=False):
    i = len(s0)
    j = len(s1)
    removals = []
    additions = []
    while i > 0 and j > 0:
        if i == 0:
            additions.append(s1[j-1])
            j-=1
        elif j == 0:
            removals.append(s1[j-1])
            i-=1
        if s0[i-1] == s1[j-1]:
            i-=1
            j-=1
        else:
            if dp[i-1][j] <= dp[i][j-1]:
                additions.append(s1[j-1])
                j-=1
            else:
                removals.append(s0[i-1])
                i-=1
    removals = removals[::-1]
    additions = additions[::-1]
    print(f"{Style.RED}{len(removals)}-----{Style.RESET}")
    print(f"{Style.GREEN}{len(additions)}++++++{Style.RESET}")


if __name__ == "__main__":
    a,b = main()
    dpMatrix  = LCS(a,b)
    backtrack(dpMatrix,a,b)