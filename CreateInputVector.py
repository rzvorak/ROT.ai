import RedditAPI as reddit
import GoogleInfoMinTo30AfterDecimal as minTo30
import GoogleInfoMaxTo30AfterDecimal as maxTo30
import GoogleINFO4months as four
import GoogleCurrent as current
import pronunciation as pronounce
import warnings

def createInputVector():
    warnings.simplefilter(action='ignore', category=FutureWarning)

    def count_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)

    with open('output.txt', 'a') as fileWrite:
        with open('words.txt', 'r') as file:
            lines = file.readlines()
            for line in lines[count_lines('output.txt'):]:
                if "\n" in line:
                    line = line[:-1]
                ratio_vector = reddit.testRedditAPI(word = line)
                min = minTo30.min(word = line)
                max = maxTo30.max(word = line)
                months = four.fourMonths(word = line)
                curr = current.cur(word = line)
                pornounce = pronounce.prevalenceScore(ipa = line)
                input = [line, ratio_vector[0], ratio_vector[1], min, max, months, pornounce, curr] # Last element is output
                print(input)
                fileWrite.write(str(input))
                fileWrite.write("\n")
    