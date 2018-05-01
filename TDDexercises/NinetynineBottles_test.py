from 99Bottles import *

lyrics = 99 
assert is_valid_lyric(lyrics), "%s should be valid" % beerbottles 

lyrics2 = 'a'
assert not is_valid_lyric(lyrics2), "a is not a valid beer bottle number"

lyrics3 = 100
assert not is_valid_lyric(lyrics3), "100 is too many bottles of beer"

