import os


def main():
    """This is the entry point"""
    value = os.getenv('SAMPLE_VALUE', 'sample')
    print(value)
    return value

main()
