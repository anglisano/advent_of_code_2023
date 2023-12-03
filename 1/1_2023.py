r'''
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your puzzle answer was 53386.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''
import re
from pathutility import PathUtils
pu=PathUtils()

def readlines(file_path:str):
    with open(file_path) as f:
        lines=f.readlines()
    return lines

def transform_line(line:str):
    dict_transform={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    for key,value in dict_transform.items():
        line=line.replace(key,str(value))
    return line

# numbers=(r'one',r'two',r'three',r'four',r'five',r'six',r'seven',r'eight',r'nine')
# newregex=r'{}'.format('|'.join(numbers))
# pattern=r'\d|{}'.format(newregex)
def get_digits(line:str):
    # line=transform_line(line)
    digits=re.findall(r'\d',line)
    # transfrom_digits=[transform_line(digit) for digit in digits]

    return digits

def get_digits2(line: str):
    digit_pattern = r'\d'
    spelled_out_pattern = r'one|two|three|four|five|six|seven|eight|nine'

    # digits = re.findall(digit_pattern, line)
    spelled_out = re.findall(spelled_out_pattern, line)

    transformed_line = line
    for spelled_num in spelled_out:
        transformed_line = transformed_line.replace(spelled_num, str(transform_line(spelled_num)), 1)

    final_digits = re.findall(digit_pattern, transformed_line)
    return final_digits

def get_first_and_last_digits(line:str):
    # digits=get_digits(line)
    digits=get_digits2(line)
    first_digit=digits[0]
    last_digit=digits[-1]
    return first_digit,last_digit

def get_two_digit_number(line:str):
    first_digit,last_digit=get_first_and_last_digits(line)
    two_digit_number=first_digit+last_digit
    return two_digit_number

def main(file_path:str):
    lines=readlines(file_path)
    sum=0
    for line in lines:
        two_digit_number=get_two_digit_number(line)
        print(two_digit_number)
        sum+=int(two_digit_number)
    return sum
if __name__ == "__main__":
    # get_digits2('eightwothree\n')
    # file_path=r'1\example.txt'
    # sum=main(file_path)
    # print(f'for the file {pu.get_filename(file_path)} the sum is {sum}')# 53386
    file_path=r'1\example2.txt'
    sum=main(file_path)
    print(f'for the file {pu.get_filename(file_path)} the sum is {sum}')

    file_path=r'1\input.txt'
    sum=main(file_path)
    print(f'for the file {pu.get_filename(file_path)} the sum is {sum}')
    pass