

import os


def main():
    value = os.getenv('SAMPLE_VALUE', 'sample')
    print(value)
    return value

main()
