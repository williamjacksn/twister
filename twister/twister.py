import argparse
import random
import subprocess
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser()

    air_help = 'include \'in the air\' as a valid action'
    parser.add_argument('-a', '--air', action='store_true', help=air_help)

    delay_help = ('number of seconds to wait before automatically showing the '
                  'next move (specifying -d with no value will use the default '
                  'value of 10 seconds)')
    parser.add_argument('-d', '--delay', nargs='?', const=10, type=int,
                        help=delay_help)

    talk_help = ('speak the move aloud (only supported on platforms with the '
                 '`say` command)')
    parser.add_argument('-t', '--talk', action='store_true', help=talk_help)

    return parser.parse_args()


def main():
    args = parse_args()
    parts = ['Right Foot', 'Right Hand', 'Left Foot', 'Left Hand']
    actions = ['Red', 'Yellow', 'Green', 'Blue']

    if args.air:
        print('Playing with \'in the air\' as a valid action')
        actions.append('in the air')

    if args.delay:
        m = 'Automatically showing next move after {} second'
        if args.delay > 1:
            m = '{}s'.format(m)
        print(m.format(args.delay))
    else:
        print('Press <Enter> to show the next move')

    if args.talk:
        print('Talking is activated')

    print('**')

    while True:
        try:
            move = '{} {}'.format(random.choice(parts), random.choice(actions))
            print(move)
            if args.talk:
                subprocess.call(['say', '-v', 'Samantha', '-r', '150', move])
            if args.delay:
                time.sleep(args.delay)
            else:
                input()
        except KeyboardInterrupt:
            print()
            sys.exit()


if __name__ == '__main__':
    main()
