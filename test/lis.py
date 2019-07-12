import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '..', 'algobox')))

from algobox.lis import longest_increase_sequence

print(longest_increase_sequence([1, 2, 3, 2, 43, 54, 2, 234, 3]))
